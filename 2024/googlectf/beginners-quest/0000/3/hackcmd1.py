# -*- coding: utf-8 -*-

def read_file(file_path: str) -> str:
    with open(file_path, 'r', encoding='utf-8') as f:  # Specify encoding as utf-8
        text = f.read()
    return text

def detranspose(text: str, columns: int) -> str:
    result = ''
    rows = [''] * (len(text)//columns)
    for i in range(len(text)//columns):
        for j in range(columns):
            rows[i] += text[i + j * (len(text)//columns)]

    for row in rows:
        # change order 2, 0, 3, 5, 1, 4
        result += row[2]
        result += row[0]
        result += row[3]
        result += row[5]
        result += row[1]
        result += row[4]
    return result

# Input text
text = "rs␣r␣enigm␣␣aierhe␣i␣gluucsclhetersnti␣a␣rla␣t␣riayrgpetai␣diu␣Fawhiho}sipatfy␣ihr␣a␣rfa␣pes␣etohwrea␣octtonee␣eihetTpxcdeghi␣ro␣ped␣yGaledemXToneepetlhtseghectnatanst␣ripctiharaics␣foarscee␣ebrn␣te␣doemrr␣c__ltcsaicsa␣coo␣wbrn␣␣aranmeibti,haarhra,sipklti␣ci.ctst␣a␣lxtcnaenlkLeoakelXpohry␣patakrntd␣cilxsU␣inehe␣cwthers␣rpo␣narahhtr␣aienlsrtrr␣o.{rd___nXnti␣␣ornrtoyrgoors␣te.ksip␣␣crs␣␣c␣pohelhgctn␣ie␣erntatecg␣teeeAsuvesuX"
columns = 6

# Convert the text using the detranspose function
converted_text = detranspose(text, columns).replace('␣', ' ')

# Output the converted text
print(converted_text)

