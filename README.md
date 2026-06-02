# 日常習慣「隱形開銷」與微型理財儀表板

**Micro-Finance & Expense Optimizer**

把每天不經意花掉的小錢，轉換成薪資分配、長期複利機會成本與具體生活目標。

## 專案概述

本專案聚焦於個人日常生活中的「隱形開銷」，也就是常被稱為拿鐵因子的微小習慣支出。透過一套標準化 Skill 工作流程，將手搖飲、咖啡、外送、少用訂閱等支出轉換為月平均、年支出、複利未來價值，並進一步拆解成可感知的夢想 BOM 購買力。

這個 repository 同時包含：

| 類型 | 說明 | 主要檔案 |
| :--- | :--- | :--- |
| **Skill 工作流程** | 定義資料清洗、分類、標準化與複利計算邏輯 | `SKILL.md` |
| **互動式作品** | 可直接開啟的微型理財儀表板 | `index.html`, `styles.css`, `script.js` |
| **CSV 工具** | 用 Python 分類記帳 CSV | `scripts/process_expenses.py` |
| **範例資料** | 可用於測試匯入功能 | `examples/sample-expenses.csv` |

## 功能亮點

* 輸入月薪、必要支出、每日/每週/每月隱形開銷。
* 使用滑桿調整「降級消費比例」、「年化報酬率」、「觀察年限」。
* 匯入日常記帳 CSV，依關鍵字自動分類必要支出與隱形開銷。
* CSV 匯入後顯示分類結果摘要，包含各類筆數與最大筆隱形開銷。
* 依照降級消費比例顯示痛感等級，協助判斷調整幅度是否容易維持。
* 提供目標選擇器，估算以目前每月新增儲蓄需要幾個月達成指定目標。
* 使用原生 CSS `conic-gradient` 繪製薪資分配圓餅圖，不依賴外部 CDN。
* 使用原生 SVG 繪製複利資產累積折線圖。
* 將期滿累積金額換算為台東兩天一夜遊、曼谷旅遊、歐洲旅遊、專業運動設備、看一次演唱會與吃一次島語的購買力。

---

## 快速開始

直接用瀏覽器開啟：

```text
index.html
```

> 本專案不需要後端、不需要安裝套件，也不需要建置流程。上傳到 GitHub Pages 後即可作為靜態網站使用。

---

## CSV 匯入格式

儀表板支援匯入日常記帳 CSV。建議欄位如下：

```csv
date,description,amount
2026-05-01,咖啡,80
2026-05-02,房租,16000
2026-05-03,Netflix 訂閱,390
```

範例檔案：

```text
examples/sample-expenses.csv
```

CSV 分類邏輯會依照 `description` 欄位中的關鍵字進行判斷：

| 分類 | 範例關鍵字 |
| :--- | :--- |
| **必要支出** | 房租、租金、水電、健保、保險、學貸、交通、捷運、雜貨 |
| **隱形開銷** | 咖啡、拿鐵、手搖、飲料、訂閱、外送、點心、宵夜、Netflix、Spotify |
| **其他支出** | 未命中上述規則的項目 |

---

## Python CSV 清洗工具

除了網頁匯入，也可以用 Python 腳本在命令列中處理 CSV：

```bash
python scripts/process_expenses.py examples/sample-expenses.csv
```

輸出內容包含：

* `monthly_average`：必要支出、隱形開銷與其他支出的月平均
* `totals`：各分類總額
* `counts`：各分類筆數
* `month_count`：CSV 橫跨月份數
* `rows`：每筆資料的分類結果

---

## 核心公式

將不同頻率的支出轉換為月支出：

```text
E_month = (E_day * 30.4) + (E_week * 4.33) + E_fixed_monthly
```

年支出：

```text
E_year = E_month * 12
```

每月新增可儲蓄金額：

```text
E_month_saved = E_hidden_month * downgrade_ratio
```

複利未來價值：

```text
FV = E_month_saved * (((1 + r / 12)^(12n) - 1) / (r / 12))
```

其中：

* `r`：年化報酬率
* `n`：觀察年限
* `downgrade_ratio`：降級消費比例

---

## 夢想 BOM 表

儀表板會把期滿複利累積金額換算成具體購買力：

| 類別 | 拆解邏輯 |
| :--- | :--- |
| **台東兩天一夜遊** | 台東 2 天 1 夜小旅行：來回交通、住宿 1 晚、餐飲與在地交通 |
| **曼谷旅遊** | 曼谷自由行套組：來回機票、BTS 交通、住宿 |
| **歐洲旅遊** | 歐洲 10 日自由行套組：來回機票、住宿、城市交通與火車、景點與餐飲緩衝 |
| **專業運動設備** | 高階羽球拍、線與握把布、保護套 |
| **看一次演唱會** | 以單人票券、交通與現場開銷估算，座位區域可依實際票價調整 |
| **吃一次島語** | 以單人餐費含服務費約 NT$2,000 估算，可作為短期無痛目標 |

> BOM 金額是可調整的生活化估算，目的是讓長期複利金額更有感；實際價格可依旅行季節、餐期、店內公告或個人需求調整。

---

## 檔案結構

```text
.
├── index.html
├── styles.css
├── script.js
├── SKILL.md
├── README.md
├── LICENSE
├── examples/
│   └── sample-expenses.csv
└── scripts/
    └── process_expenses.py
```

---

## 部署建議

1. 將此 repository 上傳到 GitHub。
2. 進入 repository 的 `Settings`。
3. 開啟 `Pages`。
4. Source 選擇 `Deploy from a branch`。
5. Branch 選擇 `main`，資料夾選擇 `/root`。

完成後即可用 GitHub Pages 開啟儀表板。
