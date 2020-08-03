# 南藝大打工仔登錄助手
## 簡介
作為修復壁畫的打工仔需要不厭其煩地到南藝大登錄系統手動輸入自己的打工紀錄，規定說每日不得超過八小時，每週不得超過四十小時，不過我沒有寫時數計算跟連續工作天數超出規定的提示功能就是了。

每天的工作紀錄得拆成上午和下午兩個時段，而工作內容的敘述是一樣的，如此重複的複製貼上是如此乏味，所以我寫了這支簡單的 Chrome Driver 幫我登錄資料，使用者可能會需要調整參數，因此我沒有包成 `exe` 檔，另一個原因是我有點懶惰。



## 環境建置
1. 安裝 Python

    下載 `Python 3.8.4 64bits` 版，點這個[連結](https://www.python.org/ftp/python/3.8.4/python-3.8.4-amd64.exe)就可以下載了。以下為示意圖，並非前面給的連結的版本（因為我已經安裝好了），安裝時需要勾選將 `python` 加入 `PATH`，然後按 Install Now ，若有安裝 `pip` 的選項記得打勾，之後安裝完即可。

    ![](https://i.imgur.com/oxzXaiC.png)

2. 檢查 python 是否安裝完成
    
    按壓鍵盤 `Windows` 鍵 + `R`，輸入 `cmd` 後按下 `Enter` 打開命令提示字元。
    
    ![](https://i.imgur.com/REG9lUu.png)

    
3. 在命令提示字元輸入 `python --version` 檢查 `python` 版本

    ![](https://i.imgur.com/PQHs36C.png)
    
4. 點擊 Git repo 上方的 `clone`，將這個程式下載到你的電腦上並解壓縮，建議路徑不要有中文。
    
    ![](https://i.imgur.com/qoWO37o.png)

5. 回到命令提示字元輸入，將路徑切換至剛剛下載的路徑。

    * 若路徑在C槽內，如 `C:\GitHub\TNNUA_work_keyin_assistant`，直接輸入 `cd GitHub\TNNUA_work_keyin_assistant`。
    * 若路徑在D槽內，如 `D:\GitHub\TNNUA_work_keyin_assistant`，請先輸入 `D:` 並按下 `Enter`，即可切換到D槽，之後再輸入 `cd GitHub\TNNUA_work_keyin_assistant`。

        路徑在D槽的示意圖：![](https://i.imgur.com/37sQoWZ.png)

    
6. 輸入 `pip install -r requirements.txt`。

    這個指令將會安裝這個程式所需要的套件。截圖中，可以看到路徑前面多了個`(venv)`和你不太一樣，這是由於我已經有安裝過了，因此開虛擬環境示範一次安裝過程，無須理會。
    
    ![](https://i.imgur.com/oTsxCEA.png)

7. 安裝 Chrome Driver
    
    請點選此[連結](https://chromedriver.chromium.org/)，並按照示意圖點選下載，下載路徑選擇 `C:\Users\你的使用者名稱` 。

    ![](https://i.imgur.com/WO9Kh4j.png)

 
## 使用說明
1. `Config.ini` 設定檔
    
    打開程式資料夾，雙擊名稱為 `Config.ini` 的檔案，並依照順序：
    * 將 `PATH_TO_CHROMEDRIVER` 改為剛剛所下載的 chromedriver.exe 放置的路徑
    * 將 `YOUR_ACCOUNT` 改為登錄系統的帳號
    * 將 `YOUR_PASSWORD` 改為登錄系統的密碼
    
    ![](https://i.imgur.com/P2AL9OJ.png)

2. `main.py` 主程式
    * 舉例一：若日期為 8/17 、 8/18 及 8/20，則修改月份 `month` 引號內數字為 08，日期 `day` 中括號中刪除 `"14","15"`，加入 `"17","18","20"`。
    
        ![](https://i.imgur.com/lMp1o5a.png)
    
    * 舉例二：若上午下午的時段並非程式內設定的，自行修改 `check_in` 及 `check_out` 引號內的時間即可(引號代表字串)。

        ![](https://i.imgur.com/WoxfN0Y.png)


3. 執行程式
    在剛剛的 cmd (路徑要在程式資料夾)內輸入 `python main.py`，即可自動登錄資料。
    ![](https://i.imgur.com/GyfyhBa.png)
