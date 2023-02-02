#17249 태보태보 총난타

taebo = input()
right_face = "("
rf_position = taebo.index(right_face)
right_arm = taebo[0:rf_position]
left_face = ")"
lf_position = taebo.index(left_face)
left_arm = taebo[lf_position:len(taebo)]

r_count = right_arm.count("@")
l_count = left_arm.count("@")

print(r_count, l_count)