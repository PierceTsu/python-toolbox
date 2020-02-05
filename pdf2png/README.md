## pdf2png
* 提取PDF中的首页保存为图片

## 安装

### Mac
```bash
# 由于7.xx版本的接口改变，必须安装6.xx版本，以及GhostScript
brew install imagemagick@6


# 设置软链
ln -s /usr/local/Cellar/imagemagick@6/6.9.9-49/lib/libMagickWand-6.Q16.dylib /usr/local/lib/libMagickWand.dylib
# 添加至系统环境
echo 'export PATH="/usr/local/opt/imagemagick@6/bin:$PATH"' >> ~/.bash_profile
. ~/.bash_profile

# 安装GhostScript
brew install gs
```

### Linux
```bash
# centos
# 安装ImageMagick和GhostScript, 选择安装6.xx版本，由于依赖关系，会自动安装GhostScript
yum install ImageMagick
```

### Windows
* 步骤:
    1. 下载[ImageMagick](https://www.imagemagick.org/download/binaries/ImageMagick-6.9.10-8-Q16-x64-dll.exe)
    2. [安装配置](http://docs.wand-py.org/en/latest/guide/install.html#install-imagemagick-windows)
    3. 下载安装[GhostScript](https://www.ghostscript.com/download/gsdnld.html)
* 说明:
    1. windows环境下配合Wand0.4.4使用的时候，加载Wand后，python读取的环境变量Path变成了unicode类型，导致启动webdirver时会报“TypeError: environment can only contain strings”，可以在引入Wand后，将path修改回str类型
    ```python
    import os
    import wand
    os.environ['path'] = str(os.environ['path'])
    ```
    
## 使用

### 安装python模块
```bash
pip install -r requirements.txt
```

### 运行
```bash
# -dir 后面参数为pdf文件的文件夹路径
python main.py -dir /Users/patricktsu/Desktop/Test
```
