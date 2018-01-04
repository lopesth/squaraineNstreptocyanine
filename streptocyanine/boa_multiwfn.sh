for funcional in funcional1-base1 funcional1-base2 funcional2-base1 funcional2-base2; do
	cd $funcional
	cd BOA
	for case in case1 case2 case3; do
		cd $case
		for molecule in 5C; do
			cd $molecule
			cd Form_Checkpoint
			echo "9" > echofile_mulliken
			echo "3" >> echofile_mulliken
			echo "y" >> echofile_mulliken
			echo "0" >> echofile_mulliken
			echo "" >> echofile_mulliken
			echo "" >> echofile_mulliken
			for i in `ls *.fchk | sed 's/.fchk//g'`; do
				Multiwfn $i".fchk" < echofile_mulliken
				mv bndmat.txt $i"_bndmat_mulliken.txt"
			done
			cd ..
			cd ..
		done
		cd ..
	done
	cd ..
	cd ..
done
