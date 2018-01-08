echo "Beginning the AIMALL calculations."
for i in `ls *.fchk`; do
    echo $i
    aimqb.ish -nogui -nproc=6 -naat=3 $i
done
echo "The AIMALL calculations over."