def zbl_table(filename):
    data = []
    with open(filename, 'r') as f:
        lines = f.readlines()
        current_data = []
        for line in lines:
            if line.startswith("N"):
                if current_data:
                    data.append(current_data)
                    current_data = []
            else:
                try:
                    idx, r, energy, force = map(float, line.split())
                    current_data.append([idx, r, energy])
                except:
                    pass
        if current_data:
            data.append(current_data)

    # Rearrange the data for writing out
    out_data = []
    for i in range(len(data[0])):  # assuming each dataset has the same length
        out_row = [data[0][i][1]]  #r
        for dataset in data:
            out_row.append(dataset[i][2])  # energy
        out_data.append(out_row)

    # Write to the new file
    with open("zbl_table.txt", 'w') as f:
        for row in out_data:
            f.write(" ".join(map(str, row)) + "\n")

zbl_table("zbl.txt")

