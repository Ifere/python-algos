# BrowserHistory bh = new BrowserHistory( );
# bh.get_current_url() // returns None
# bh.go_to(“www.google.com”) // navigates to google.com
# bh.get_current_url() // returns “www.google.com”
# bh.go_to(“www.twitter.com”) // navigates to twitter.com
# bh.go_to(“www.twitter.com/dsalagos”) //navigates to www.twitter.com/dsalagos
# bh.back() // goes back
# bh.get_current_url() // returns “www.twitter.com”
# bh.forward()
# bh.get_current_url() // returns “www.twitter.com/dsalagos”
# bh.jump_to(“www.google.com”) // jumps back to “www.google.com”
# bh.forward() // moves forward to www.twitter.com, as this is the next url after we added
# “www.google.com”

# class Stack:
#     def __init__(self):
#         self.elements = []
#         self.others = []
#         self.history = {}
#
#     def get_current_url(self):
#         if not self.elements:
#             return None
#         else:
#             return self.elements[-1]
#
#     def go_to(self, url):
#         self.elements.append(url)
#
#     def back(self):
#         self.elements.pop()
#         self.others.append(self.elements.pop())
#
#     def forward(self):
#         self.elements.append(self.others.pop())
#
#     def jump_to(self):

#
# class BrowserHistory:
#
#     def __init__(self):
#         self.log = {}
#         self.history = []
#         self.currentindex = -1
#
#     def get_current_url(self):
#         if not self.history:
#             return None
#         else:
#             return self.history[self.currentindex]
#
#     def go_to(self, url):
#         self.currentindex += 1
#         self.history.append(url)
#         self.log[url] = self.currentindex
#
#     def back(self):
#         if self.currentindex - 1 >= 0:
#             self.currentindex -= 1
#
#     def forward(self):
#         if self.currentindex + 1 < len(self.history):
#             self.currentindex += 1
#
#     def jump_to(self, url):
#         if url not in self.log.keys():
#             print("URL not found")
#         else:
#             self.currentindex = self.log[url]
#

# c = [1,2,3]
# c.
#
# for i in range(1, len(c)):
#     print(c[i])

class TreeNode:
    def __init__(self, x):
        self.root = x
        self.left = None
        self.right = None