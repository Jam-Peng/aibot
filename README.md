# 聊天機器人
### 初始化本地倉庫
-  git init 

- ### 檢查目前倉庫狀態
-   git status 

### 加入需要管理的程式檔案
-  git add 指定的文件.py  (加入指定檔案)
-  git add .         (加入全部檔案)

### 進行commit儲存動作

-  git commit -m "commit log"   
-  git commit -am "commit log"  增加發布 (和 -m 一樣)
 
### 檢視目前commit歷程

- git log  	

### 綁定雲端倉庫url 

-  git add remote  https://www.github.com/17app001/xxxxx

- git remote -v

### 推送程式碼

- git push


#### ===================================================

### 新增雲端倉庫後會出現
- git remote add origin git@github.com:Jam-Peng/aibot.git

### 推送(第一次) - 要使用 master 盡量不要使用main
- git push -u origin master
