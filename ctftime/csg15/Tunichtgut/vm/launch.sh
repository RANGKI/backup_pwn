#!/bin/bash
set -euo pipefail

disk=''
iso=''
flag=''
ssh=''
writable=0
extra=()
while [ "$#" -gt 0 ]; do
    case "$1" in
        --help)     echo "usage: launch.sh --disk=<disk> [--flag=<flag-file>] [--iso=<iso>] [--ssh=<port>] [--writable] [-- QEMU options]"; exit 0;;
        --disk=*)   disk="${1#--disk=}";;
        --iso=*)    iso="${1#--iso=}";;
        --flag=*)   flag="${1#--flag=}";;
        --ssh=*)    ssh="${1#--ssh=}";;
        --writable) writable=1;;
        --)         shift; extra=("$@"); break;;
        -*)         echo "unknown option: $1 (try --help)"; exit 1;;
        *)          echo "unexpected argument: $1 (try --help)"; exit 1;;
    esac
    shift
done

ports="hostfwd=tcp::1024-:1024"
if [ -n "${ssh}" ]; then ports="${ports},hostfwd=tcp::${ssh}-:22"; fi

args=(
    -enable-kvm
    -m 512M
    -smp 2
    -nographic
    -no-reboot
    -device virtio-net-pci,netdev=net0
    -netdev user,id=net0,"${ports}"
    -drive if=virtio,file="${disk}",format=qcow2
)

if [ -z "${disk}" ]; then echo 'No disk image specified (--disk=...)' >&2; exit 1; fi
if [ -n "${flag}" ]; then args+=(-drive if=virtio,file="${flag}",format=raw,id=flag); fi
if [ -n "${iso}" ]; then args+=(-cdrom "${iso}"); fi
if [ "${writable}" -le 0 ]; then args+=(-snapshot); fi
args+=("${extra[@]}")

set -x
exec qemu-system-x86_64 "${args[@]}"
