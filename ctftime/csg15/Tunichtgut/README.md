For $reasons, this challenge is hosted inside of a VM. You can reproduce the VM setup (inside a Docker container) using the following steps:

 1. Build the VM disk image using `vm/build.sh`
 2. Run the Docker container using `docker compose up`.

You can also run the challenge locally by running `docker compose up` inside the `docker` directory.
This will likely make things easier to debug, and save you several gigabytes worth of disk space.
