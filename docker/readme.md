```
docker build -t my_ubuntu_ssh .
docker run -itd -p 2223:22 --name my_ubuntu_container my_ubuntu_ssh
```