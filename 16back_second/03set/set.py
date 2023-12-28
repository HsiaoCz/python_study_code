# 不可变序列:字符串和元组
# 可变序列：列表和字典
# 所谓可变：就是改变内容之后内存地址不会发生变化
# 所谓不可变，就是改变内容之后，内存地址发生了变化
# 这里有一个疑问。集合是不是可变序列
# 这里集合好像是可变序列
ss={"hello","hi"}
print(id(ss))
ss.add("hihi")
print(id(ss))
ss.add("jij")
print(id(ss))
ss.add("hhihhh")
print(id(ss))

tt=("hekko","hii")
print(id(tt))
tt=("hekko","hii","hiii")
print(id(tt))