
#python
import sys
sys.path.append('/home/solup/Desktop/blog')  # This is an absolute path
import blog
import os
import string
import collections
import zipfile
import tempfile
import subprocess

def gather_crcs_from_zip(zip_file, targets, crcs, limit):
    with zipfile.ZipFile(zip_file) as fh:
        for info in fh.infolist():
            targets[f'{zip_file} / {info.filename}'] = (info.CRC, info.file_size)
            crcs.append((info.CRC, info.file_size))
            limit = max(limit, info.file_size)
            print(f'file found: {zip_file} / {info.filename}: crc = 0x{info.CRC:08x}, size = {info.file_size}', file=sys.stderr)
    return limit

def solve_crcs(crcs, targets, limit, compiler='g++', alphabet=string.printable.encode()):
    # Compile C++ code
    code = ''
    code += r'''
    #include <cstdio>
    #include <vector>
    #include <array>
    #include <string>
    #include <set>
    #include <cstdint>
    #include <cctype>
    #define repeat(i,n) for (int i = 0; (i) < (n); ++(i))
    using namespace std;

    uint32_t crc_table[256];
    void make_crc_table() {
        repeat (i, 256) {
            uint32_t c = i;
            repeat (j, 8) {
                c = (c & 1) ? (0xedb88320 ^ (c >> 1)) : (c >> 1);
            }
            crc_table[i] = c;
        }
    }
    const uint32_t initial_crc32 = 0xffffffff;
    uint32_t next_crc32(uint32_t c, char b) {
        return crc_table[(c ^ b) & 0xff] ^ (c >> 8);
    }
    const uint32_t mask_crc32 = 0xffffffff;

    const char alphabet[] = { ''' + ', '.join(map(str, alphabet)) + r''' };
    const int limit = ''' + str(limit) + r''';

    array<set<uint32_t>, limit+1> crcs;
    string stk;
    void dfs(uint32_t crc) {
        if (crcs[stk.length()].count(crc ^ mask_crc32)) {
            fprintf(stderr, "crc found: 0x%08x: \"", crc ^ mask_crc32);
            for (char c : stk) fprintf(stderr, isprint(c) && (c != '\\') ? "%c" : "\\x%02x", c);
            fprintf(stderr, "\"\n");
            printf("%08x ", crc ^ mask_crc32);
            for (char c : stk) printf(" %02x", c);
            printf("\n");
        }
        if (stk.length() < limit) {
            for (char c : alphabet) {
                stk.push_back(c);
                dfs(next_crc32(crc, c));
                stk.pop_back();
            }
        }
    }

    int main() {
    '''
    for crc, size in crcs:
        code += '    crcs[' + str(size) + '].insert(' + hex(crc) + ');\n'
    code += r'''
        make_crc_table();
        dfs(initial_crc32);
        return 0;
    }
    '''

    with tempfile.TemporaryDirectory() as tmpdir:
        cppname = os.path.join(tmpdir, 'a.cpp')
        with open(cppname, 'w') as fh:
            fh.write(code)
        binname = os.path.join(tmpdir, 'a.out')
        print('compiling...', file=sys.stderr)
        subprocess.check_call([compiler, '-std=c++11', '-O3', '-o', binname, cppname])
        print('searching...', file=sys.stderr)
        p = subprocess.Popen([binname], stdout=subprocess.PIPE)
        output, _ = p.communicate()

    print('done', file=sys.stderr)
    print(file=sys.stderr)
    result = collections.defaultdict(list)
    for line in output.decode().strip().split('\n'):
        crc, *val = map(lambda x: int(x, 16), line.split())
        result[(crc, len(val))] += [bytes(val)]
    for key, crc in targets.items():
        for s in result[crc]:
            print(f'{key} : {repr(s)[1:]}')

def solve(zip_file, hex_values=None, dec_values=None, limit=None, compiler='g++', alphabet=string.printable.encode()):
    targets = collections.OrderedDict()
    crcs = []

    if limit is None:
        raise ValueError('Limit of length not specified')
    if hex_values:
        for s in hex_values:
            crc = int(s, 16)
            targets[s] = crc
            for l in range(limit + 1):
                crcs.append((crc, l))
    if dec_values:
        for s in dec_values:
            crc = int(s)
            targets[s] = crc
            for l in range(limit + 1):
                crcs.append((crc, l))

    with tempfile.TemporaryDirectory() as tmpdir:
        nested_zip_files = []
        with zipfile.ZipFile(zip_file, 'r') as zip_ref:
            zip_ref.extractall(tmpdir)
            for root, _, files in os.walk(tmpdir):
                for file in files:
                    if file.endswith('.zip'):
                        nested_zip_files.append(os.path.join(root, file))

        if not nested_zip_files:
            limit = gather_crcs_from_zip(zip_file, targets, crcs, limit)
        else:
            for nested_zip in nested_zip_files:
                limit = gather_crcs_from_zip(nested_zip, targets, crcs, limit)

    if not crcs:
        raise ValueError('No CRCs given')

    solve_crcs(crcs, targets, limit, compiler, alphabet)

if __name__ == "__main__":
    outer_zip_file = blog.set("flag_parts.zip",1)  # Update this to the path of the outer ZIP file containing the flag ZIP files
    solve(outer_zip_file, hex_values=["1a2b3c4d"], dec_values=["12345678"], limit=4)
