import subprocess
import sys
import os

def install_package(package_name):
    try:
        __import__(package_name)
        return True, f"✅ {package_name} 已安装"
    except ImportError:
        print(f"🔄 正在安装 {package_name}...")
        try:
            subprocess.check_call([
                sys.executable, "-m", "pip", "install", 
                package_name, 
                "-i", "https://pypi.tuna.tsinghua.edu.cn/simple"
            ])
            return True, f"✅ {package_name} 安装成功"
        except subprocess.CalledProcessError:
            return False, f"❌ {package_name} 安装失败"

print("="*60)
print("OneQuant ZeroCode Pro V3.0.0 一人公司量化交易系统")
print("="*60)
print()
print("正在检查基础依赖...")
print("-"*60)

# 只安装最基础的依赖，确保系统能启动
base_deps = ["flask", "flask-cors", "pandas", "numpy"]

all_success = True
for dep in base_deps:
    success, msg = install_package(dep)
    print(msg)
    if not success:
        all_success = False

print("-"*60)
if all_success:
    print("✅ 基础依赖安装完成！")
else:
    print("⚠️ 部分依赖安装失败，系统可能无法正常运行")

print()
print("📌 数据源依赖安装说明：")
print("• 米筐：pip install rqsdk && rqsdk install rqdatac")
print("• 聚宽：pip install jqdatasdk")
print("• Tushare：pip install tushare")
print()
print("="*60)
print("系统正在启动...")
print("启动成功后，请打开浏览器访问：http://127.0.0.1:5000")
print()
print("⚠️ 请勿关闭此窗口，关闭将停止系统运行")
print("="*60)
print()

# 启动Web服务器
try:
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    subprocess.call([sys.executable, "web_server_v4.py"])
except Exception as e:
    print(f"❌ 系统启动失败：{e}")
    print()
    input("按回车键退出...")
