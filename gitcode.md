# 进入本地项目文件夹
cd F:\learn\myenv\shserverenv\shenv
 
# 初始化本地仓库
git init
 
# 添加文件到本地仓库
git add .
 
# 提交改动到本地仓库
git commit -m "Initial commit"
 
# 添加远程仓库地址（将YOUR_USERNAME和YOUR_REPO替换为实际的用户名和仓库名）
git remote add origin git@github.com:lim0098/shenv.git
 
# 推送本地仓库到GitHub远程仓库
git push origin master

# 远程仓库取到本地 . 代表当前路径
git clone <远程仓库URL> <本地路径>
git clone git@github.com:lim0098/shenv.git .
# 新建python虚拟环境
python -m venv shenv

