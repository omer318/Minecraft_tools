import re
def sub_list(sub,all):
    for i in sub:
        for j in all:
            if i==j:
                all.remove(j)
    return all

def cleanfile(s):
    s=s.lower()
    s = re.sub(r"\"minecraft:|[0-9]|\"|:| |-|,|\+|textures/entity/cat/|.png", "", s)
    s = re.sub("_", " ", s)
    s=re.sub("\n\n","\n",s)
    return s.split("\n")


def main():
    all_b = open('C:\\Users\\user\\Desktop\\AllBiomes.txt', 'r')
    my_b = open('C:\\Users\\user\\Desktop\\MyBiomes.txt', 'r')
    str_all = cleanfile(all_b.read())
    str_my = cleanfile(my_b.read())
    str_all.sort()
    str_my.sort()
    l=sub_list(str_my,str_all)
    print("{}\n\n\n{}\n\n\n{}".format(str_all,str_my ,l))


if __name__ == '__main__':
    main()
