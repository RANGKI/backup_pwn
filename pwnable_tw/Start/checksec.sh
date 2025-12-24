# check for NX support
  $debug && echo -e "\n***function filecheck->nx"
  if $readelf -W -l "$1" 2>/dev/null | grep -q 'GNU_STACK'; then
    if $readelf -W -l "$1" 2>/dev/null | grep 'GNU_STACK' | grep -q 'RWE'; then
      echo '\033[31mNX disabled\033[m   ' 'NX disabled,' ' nx="no"' '"nx":"no",'
    else
      echo '\033[32mNX enabled \033[m   ' 'NX enabled,' ' nx="yes"' '"nx":"yes",'
    fi
  else
    echo '\033[31mNX disabled\033[m   ' 'NX disabled,' ' nx="no"' '"nx":"no",'
  fi
