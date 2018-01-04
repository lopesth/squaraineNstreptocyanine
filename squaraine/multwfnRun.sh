echo "9" > echofile_mulliken
echo "4" >> echofile_mulliken
echo "y" >> echofile_mulliken
echo "0" >> echofile_mulliken
echo "" >> echofile_mulliken
echo "" >> echofile_mulliken

echo "9" > echofile_Wiberg
echo "3" >> echofile_Wiberg
echo "y" >> echofile_Wiberg
echo "0" >> echofile_Wiberg
echo "" >> echofile_Wiberg
echo "" >> echofile_Wiberg

echo "9" > echofile_Mayer
echo "1" >> echofile_Mayer
echo "y" >> echofile_Mayer
echo "0" >> echofile_Mayer
echo "" >> echofile_Mayer
echo "" >> echofile_Mayer  

for i in `ls *.fchk | sed 's/.fchk//g'`; do
	Multiwfn $i".fchk" < echofile_mulliken
	mv bndmat.txt $i"_bndmat_mulliken.txt"
    Multiwfn $i".fchk" < echofile_Wiberg
    mv bndmat.txt $i"_bndmat_wiberg.txt"
    Multiwfn $i".fchk" < echofile_Mayer
    mv bndmat.txt $i"_bndmat_mayer.txt"
done