iris2 = iris.copy()
iris2_grouped = iris2.groupby(iris2.variety)
with pd.ExcelWriter('iris2.xlsx') as writer:
    iris2_grouped.get_group("Setosa").to_excel(writer, sheet_name="Setosa")
    iris2_grouped.get_group("Versicolor").to_excel(writer, sheet_name="Versicolor")
    iris2_grouped.get_group("Virginica").to_excel(writer, sheet_name="Virginica")