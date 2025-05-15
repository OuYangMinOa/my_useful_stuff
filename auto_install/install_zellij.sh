git config --global http.sslbackend gnutls
curl https://sh.rustup.rs -sSf | bash -s -- -y
echo 'source $HOME/.cargo/env' >> $HOME/.bashrc
PATH="/root/.cargo/bin:${PATH}"
/root/.cargo/bin/cargo install --locked zellij