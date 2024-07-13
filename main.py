import streamlit as st


def jump_str(content: str, url: str) -> str:
    return f"<a href=\"{url}\">{content}<a/>"


text = st.write
index = st.session_state.get("index", default=0)
st.title("Python教程")
steps = ["1.下载Python",
         "2.下载一个好用的编辑器",
         "3.创建项目",
         "4.简单认识",
         "更多:等待更新",]
page = st.selectbox(label="步骤", options=steps, index=index)
st.divider()
match steps.index(page):
    case 0:
        text(" ")
        text("在学习Python之前,你需要先下载一个Python.")
        text(" ")
        st.divider()
        st.header("目标:下载Python 3.12.4并安装.注意要添加到环境变量,从官网下载.")
        st.divider()
        text("出于提高自主学习能力的目的,请先尝试自行完成该目标.如遇到困难,可点击下方按钮查看详细说明.")
        if st.button("详细说明"):
            st.balloons()
            text("Python官网网址为:https://www.python.org/")
            text("下载Python")
            st.image("1.png")
            st.image("2.png")
            text("下载过慢的话,试试其他工具?(如把链接复制到迅雷中下载)")
            st.divider()
            text("安装Python")
            for i in range(3, 7):
                st.image(f"{i}.png")
            text("第一次装的话点一下这个选项.")
            text("恭喜,安装完成!")
            text("按下windows+r,输入cmd并回车打开命令提示符,输入python")
            st.image("7.png")
            text("如图所示,你已成功安装python.🎈🎈🎈🎈")
    case 1:
        text(" ")
        text("使用优秀的编辑器是提高效率的最佳手段,可以为你提供代码补全等强大的功能.工欲善其事,必先利其器.")
        text(" ")
        st.divider()
        st.header("目标:安装一个好用的编辑器.(推荐: Pycharm)")
        st.divider()
        text("出于提高自主学习能力的目的,请先尝试自行完成该目标.如遇到困难,可点击下方按钮查看详细说明.")
        if st.button("详细说明"):
            st.balloons()
            text("此处以Pycharm为例.")
            text("Pycharm官网:https://www.jetbrains.com.cn/pycharm/download/?section=windows")
            st.image("8.png")
            text("社区版就OK,专业版要花钱,而且我想你也用不到(滑稽)")
            text("emmm...\n我不能同时装两个Pycharm,也不能卸了重装一遍,所以只能给你指一个教程了.")
            text("https://blog.csdn.net/2301_78096295/article/details/139240616")
            text("安装Chinese插件以汉化.")
            st.image("9.png")
    case 2:
        text("以Pycharm为例.请下载以下视频并观看.(当然先自己摸索一下更好)")
        st.download_button("下载视频", data=open("1.mp4", "rb"), file_name="1.mp4")
    case 3:
        text("Python中的一切都是由类构成的，不过现在你姑且可以认为分为变量(variable)、函数(function)、类(class)三大类。")
        text("Python中最基础的函数有print、input等；最基础的变量分为字符串(str)、整数(int)、浮点数(float)、列表(list)、字典(dict)、集合(set)等。")
        st.title("变量")
        text("变量以 变量名 = 变量值 的格式赋值，注意变量名需满足如下要求：")
        text("1.字母或下划线(_)开头。")
        text("2.由字母、下划线、数字构成。")
        text("3.大小写字母不同时，变量也不相同。(如Hello和hello是两个不同的变量)")
        st.subheader("例:")
        text(f"合法的变量名: {'、'.join(['Hello', 'a', 'b', '_len', 'test2'])}等")
        text(f"不合法的变量名: {'、'.join(['3hello', '你好', 'hello*', '#a'])}等")
        text("变量赋值例子:(在Python解释器中输入)")
        text("在pycharm项目中点击左边栏下侧Python控制台或在开始菜单中打开Python")
        st.code(""">>>a = 100
>>>b = "Hello world"
>>>c = [1, 2, 3, 4, 5]
>>>d = a
>>>e = b
>>>a
100
>>>b
'Hello world'
>>>c
[1, 2, 3, 4, 5]
>>>d
100
>>>e
'Hello world'""")
        st.divider()
        st.title("函数")
        text("函数的内容多种多样，这里先讨论内置函数.")
        text("内置函数就是Python中预先定义好的函数,包括输入输出、计算、数据处理、读写文件等方面的基础操作.")
        text("以下是一些需要掌握的基础函数,点击跳转至相应内容.")
        text("注意:以下示例代码均在python项目中运行,请复制代码后粘贴在项目文件中运行.")
        st.image("10.png")
        text(jump_str("input", "#input"), unsafe_allow_html=True)

        st.subheader("input")
        st.text("input函数可以返回一行输入的内容,可以指定提示词.如:")
        st.code("a = input(\"输入算式\")\nb = eval(a)\nprint(a)\nprint(b)")
        st.text("运行结果")
        st.code("")
