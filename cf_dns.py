import requests
import csv

# ##################################################
# 请在这里替换您的 Cloudflare 账户信息
# ##################################################
API_KEY = ""  # 您的 Cloudflare API 密钥
EMAIL = ""      # 您的 Cloudflare 账户邮箱
# ##################################################

def get_zones():
    """获取所有域名 (zones)"""
    url = "https://api.cloudflare.com/client/v4/zones"
    headers = {
        "X-Auth-Email": EMAIL,
        "X-Auth-Key": API_KEY,
        "Content-Type": "application/json"
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # 如果请求失败，则会抛出异常
    return response.json()["result"]

def get_dns_records(zone_id):
    """获取指定域名的所有 DNS 记录"""
    url = f"https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records"
    headers = {
        "X-Auth-Email": EMAIL,
        "X-Auth-Key": API_KEY,
        "Content-Type": "application/json"
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()["result"]

def main():
    """主函数"""
    try:
        zones = get_zones()
        with open("cloudflare_dns_records.csv", "w", newline="", encoding="utf-8") as csvfile:
            fieldnames = ["Zone Name", "Type", "Name", "Content", "TTL", "Proxied"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

            for zone in zones:
                zone_name = zone["name"]
                zone_id = zone["id"]
                print(f"正在获取域名 {zone_name} 的 DNS 记录...")
                dns_records = get_dns_records(zone_id)

                for record in dns_records:
                    writer.writerow({
                        "Zone Name": zone_name,
                        "Type": record["type"],
                        "Name": record["name"],
                        "Content": record["content"],
                        "TTL": record["ttl"],
                        "Proxied": record["proxied"]
                    })
        print("\n所有 DNS 记录已成功导出到 cloudflare_dns_records.csv 文件。")

    except requests.exceptions.HTTPError as err:
        print(f"API 请求失败: {err}")
    except Exception as e:
        print(f"发生错误: {e}")

if __name__ == "__main__":

    main()
