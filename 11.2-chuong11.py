def doi_truong_te(teams):
    doi_truong = teams[-1][1] if len(teams[-1]) > 1 else None
    return doi_truong

# Danh sách các đội, mỗi đội là một danh sách
teams_list = [['steven','Neena','Lex','Alexander','Bruce'],['David','Jack','Bill','Tom','Mike','Daniel'],
              ['Alexander','Adam','Payan','Kevin','sigal','mike']
]
# Chọn ra đội trưởng tệ nhất từ danh sách các đội
doi_truong_te = doi_truong_te(teams_list)
print("Đội trưởng tệ nhất là:", doi_truong_te)