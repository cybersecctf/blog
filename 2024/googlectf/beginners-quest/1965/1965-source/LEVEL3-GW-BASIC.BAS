010 PRINT "*** THE FLAG VERIFICATOR: LEVEL 3 ***"
020 PRINT "VERSION FOR MICROSOFT GW-BASIC 1983"
030 PRINT "FLAG FORMAT: FLAG{[A-Z0-9_!]*}"
040 LET PREFIX=5
050 LET FL=41
060 LET SHIFT=&H80
110 DIM F(FL)
120 PRINT "FLAG"; : INPUT U$
130 IF LEN(U$)<>PREFIX+FL+1 THEN GOTO 600
200 FC$=MID$(U$,PREFIX+1,PREFIX+FL)
230 FOR I=1 TO FL
240 F(I)=ASC(MID$(FC$,I,1))+SHIFT
250 NEXT I
300 LET ID=0
330 FOR I=1 TO FL
340 READ A$
350 IX$=MID$(A$,3,1)
360 GOSUB 700
370 LET RES=ID*16
380 IX$=MID$(A$,4,1)
390 GOSUB 700
400 RES=RES+ID
410 IF RES<>F(I) THEN GOTO 600
430 NEXT I
500 PRINT "GOOD JOB! NOW SUBMIT THE FLAG." : END
600 RESTORE
610 PRINT "THE PROVIDED FLAG IS INVALID TRY ANONTHER" : GOTO 120
700 REM *** H2D CONVERTER ***
710 IF ASC(IX$) < 64 THEN ID=VAL(IX$) : RETURN
720 ON ASC(IX$)-64 GOTO 730,740,750,760,770,780
730 ID=10 : RETURN
740 ID=11 : RETURN
750 ID=12 : RETURN
760 ID=13 : RETURN
770 ID=14 : RETURN
780 ID=15 : RETURN
900 DATA &HD3,&HD4,&HC1,&HCE,&HC4,&HC1,&HD2,&HC4,&HDF,&HC3
910 DATA &HCF,&HC4,&HC5,&HDF,&HC6,&HCF,&HD2,&HDF,&HC9,&HCE
920 DATA &HC6,&HCF,&HD2,&HCD,&HC1,&HD4,&HC9,&HCF,&HCE,&HDF
930 DATA &HC9,&HCE,&HD4,&HC5,&HD2,&HC3,&HC8,&HC1,&HCE,&HC7
940 DATA &HC5
