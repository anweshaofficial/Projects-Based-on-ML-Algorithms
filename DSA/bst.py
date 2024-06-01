def isValidBst(root, left = float('inf'),right=float('inf')):
    if not root:
        return True
    if not(left < root.val < right):
        return False
    return isValidBst(root.left, left, root.val) and isValidBst(root.right, root.val, right)

root3 = isValidBst(1)
root3.left = isValidBst(2)
root3.right = isValidBst(3)
root3.left.left = isValidBst(4)
root3.left.right = isValidBst(5)
root3.right.left = isValidBst(6)
root3.right.right = isValidBst(7)
