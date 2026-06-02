# 本地异常检测 → UiPath 云平台

> 用ngrok把本地 fastapi服务暴露到公网，将批处理检测到的异常数据发送给uipath云平台。平台收到数据后自动保存到Google Drive，同时触发邮件报告通知。

## 技术栈

- **后端**: FastAPI + Python
- **内网穿透**: ngrok
- **自动化平台**: UiPath Cloud Studio
- **存储**: Google Drive
- **通知**: 邮件报告

## 流程说明

### 本地
1. FastAPI 服务启动，通过 ngrok 暴露到公网
2. UiPath 云平台调用 API 时，传入`start_time`/`end_time`/`input_key`参数
3. `data_loader.py` 读取 `data/` 文件夹下所有 JSON 文件，按时间筛选
4. `service.py` 对筛选后的数据执行异常检测

### UiPath 云平台
5. 调用 API 获取检测结果
6. 异常数据自动保存到 Google Drive（CSV 格式）
7. 触发邮件报告通知

## 快速开始

1. **修改配置**：编辑 `main.py`，按需调整API Key等参数。

2. **启动服务**：
   - 进入项目所在目录，运行`uvicorn main:app --reload`启动fastapi
   - 另开终端，运行`ngrok http 8000`(or your location)（未安装 ngrok 请先下载配置）
3. **导入 UiPath**：登录[UiPath Cloud Studio](https://cloud.uipath.com/portal_/cloudrpa)，导入 `.uis` 文件，在 HTTP Activity 中填入你的 ngrok URL
4. **设置存储**：配置 Google Drive 授权
5. **设置邮件**：修改发件箱和收件箱地址
