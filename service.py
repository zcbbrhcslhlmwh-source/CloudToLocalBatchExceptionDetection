import pandas as pd

def detection_service(data_list):
    df = pd.DataFrame(data_list)

    #缺失值
    df["has_missing"] = df.isnull().any(axis=1)
    missing_total = df.isnull().sum().sum()

    #异常
    df["is_anomaly"] = df["temperature"] > 85
    df["is_warning"] = (df["temperature"] > 80) & (df["temperature"] <= 85)

    #连续异常
    df["rolling_alert"] = df["is_anomaly"].rolling(2).sum() >= 2

    #问题数据 
    df_problem = df[
        (df["is_anomaly"]) |
        (df["is_warning"]) |
        (df["has_missing"])
    ]
    
    #转JSON
    problem_data = df_problem.to_dict(orient="records")

    #统计
    total = len(df)
    anomaly_count = int(df["is_anomaly"].sum())
    warning_count = int(df["is_warning"].sum())
    max_temp = float(df["temperature"].max())

    summary = (
        f"共{total}条数据，"
        f"{anomaly_count}条异常，"
        f"{warning_count}条预警，"
        f"缺失值{missing_total}个，"
        f"最高温度{max_temp}℃"
    )

    return {
        "summary": summary,
        "problem_count": len(problem_data),
        "problem_data": problem_data,
    }