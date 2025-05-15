apt-get update -y
apt-get install -y git sudo curl unzip gcc ripgrep ca-certificates
git config --global http.sslbackend gnutls schannel
curl -LO https://github.com/neovim/neovim/releases/download/v0.11.0/nvim-linux-x86_64.tar.gz
rm -rf /opt/nvim
tar -C /opt -xzf nvim-linux-x86_64.tar.gz
echo 'export PATH="$PATH:/opt/nvim-linux-x86_64/bin"' >> ~/.bashrc
curl -o- https://fnm.vercel.app/install | bash
/root/.local/share/fnm/fnm install 22
mkdir ~/.config
cd ~/.config
git clone https://github.com/OuYangMinOa/neovim_setup ~/.config/nvim
rm ~/.config/nvim/lua/plugins/fold.lua
rm ~/.config/nvim/readme.md
rm -rf  ~/.config/nvim/.git
rm -rf  ~/.config/nvim/images
source ~/.bashrc
nvim --headless +qall
# git config --global http.sslbackend gnutls schannel

