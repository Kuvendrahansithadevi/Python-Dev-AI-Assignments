def build_query(**filters):
    print("->",end=" ")
    if filters=={}:
        print("(empty string)")
    for key,value in filters.items():
        last_key=list(filters.keys())[-1]
        print(f"{key}={value.strip('""')}",end="&" if key != last_key else "")
data=input()
filters=dict(item.split("=") for item in data.split(","))if data.strip() else {}
build_query(**filters)