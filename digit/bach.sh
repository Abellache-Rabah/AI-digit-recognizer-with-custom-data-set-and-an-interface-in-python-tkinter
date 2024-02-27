for i in {0..9}
do
 counter=0
 for file in $i_*
 do
   if [ $counter -lt 3 ]; then
     mv "test$file" "$file"
     let counter++
   else
     break
   fi
 done
done
