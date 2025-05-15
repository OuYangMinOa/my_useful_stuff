git config --global http.sslbackend gnutls schannel
curl -s https://ohmyposh.dev/install.sh | bash -s
echo 'export PATH=$PATH:~/.local/bin' >> ~/.bashrc
wget  https://raw.githubusercontent.com/OuYangMinOa/neovim_setup/main/myarmo.json --output-document ~/.config/nvim/myarmo.json
echo 'eval "$(oh-my-posh init bash --config ~/.config/nvim/myarmo.json)"' >> ~/.bashrc