class Solution(object):
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        flag_name = 0
        flag_typed = 0

        while flag_typed < len(typed):
            # 必须把判断是否越界放在and的前面
            if flag_name < len(name) and name[flag_name] == typed[flag_typed]:
                flag_name += 1
                flag_typed += 1
            
            # 不相同时，要注意 flag_name 指针指向的元素
            # 如果是首元素，那么表示 name 和 typed 首字符都不同，可以直接返回 False
            # 如果不在首元素，看是否键入重复，键入重复，继续移动 flag_typed 指针，继续判断；如果不重复，也就是不相等的情况，直接返回 False，表示输入错误
            elif flag_name > 0 and typed[flag_typed] == name[flag_name-1]:
                flag_typed += 1
            else:
                return False
        # typed 遍历完成后要检查 name 是否遍历完成
        return flag_name == len(name)

"""
当一号和二号路上看到的字符相同时，两人同时往前走一步。
当一号后面的字符和二号当前的字符相同时，说明typed多打了几次，二号往前走一步，一号不动。
当一号和二号看到的东西不同时，说明不对，返回False。
"""

if __name__ == "__main__":
    a = Solution()
    b = a.isLongPressedName("alex", "aaleex")
