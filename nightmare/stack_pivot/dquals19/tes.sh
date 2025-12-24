#!/bin/bash

# Meminta input absolute path dari user
read -p "Masukkan absolute path file: " file_path

# Mengekstrak nama file dari absolute path
file_name="/home/dadan/pwn/nightmare/stack_pivot/dquals19/chall"

# Mencari PID dari proses yang sesuai dengan nama file
pid=$(ps aux | grep "$file_name" | grep -v "grep" | awk '{print $2}')

# Memeriksa apakah PID ditemukan
if [ -z "$pid" ]; then
  echo "Tidak ditemukan proses dengan nama $file_name"
  exit 1
fi

# Menampilkan PID yang ditemukan
echo "PID ditemukan: $pid"

# Menjalankan gdb dengan PID yang ditemukan
gdb -p "$pid"
