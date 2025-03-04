from QuanLySinhVien import QuanLySinhVien

qlsv = QuanLySinhVien()
while (1 == 1):
    print("\nCHUONG TRINH QUAN LY SINH VIEN")
    print("*****MENU*****")
    print("1. Them sinh vien.")
    print("2. Cap nhat thong tin sinh vien boi ID.")
    print("3. Xoa sinh vien boi ID.")
    print("4. Tim kiem sinh vien theo ten.")
    print("5. Sap xep sinh vien theo diem trung binh.")
    print("6. Sap xep sinh vien theo ten chuyen nganh.")
    print("7. Hien thi danh sach sinh vien.")
    print("0. Thoat.")
    
    key = int(input("Nhap lua chon cua ban: "))
    if(key == 1):
        print("\n1. Them sinh vien.")    
        qlsv.nhapSinhVien()
        print("\nThem sinh vien thanh cong!")
    elif(key == 2):
        if(qlsv.soLuongSinhVien() > 0):
            print("\n2. Cap nhat thong tin sinh vien boi ID.")
            ID = int(input("\nNhap ID: "))
            qlsv.updateSinhVien(ID)
        else:
            print("\nDanh sach sinh vien rong. Vui long them sinh vien.")
    elif(key == 3):
        if(qlsv.soLuongSinhVien() > 0):
            print("\n3. Xoa sinh vien boi ID.")
            ID = int(input("\nNhap ID: "))
            if(qlsv.deleteByID(ID)):
                print("\nSinh vien co ID = ", ID, " da duoc xoa.")
            else:
                print("\nSinh vien co ID = ", ID, " khong ton tai.")
        else:
            print("\nDanh sach sinh vien rong. Vui long them sinh vien.")
    elif(key == 4):
        if(qlsv.soLuongSinhVien() > 0):
            print("\n4. Tim kiem sinh vien theo ten.")
            name = input("\nNhap ten sinh vien can tim: ")
            searchResult = qlsv.findByName(name)
            qlsv.showSinhVien(searchResult)
        else:
            print("\nDanh sach sinh vien rong. Vui long them sinh vien.")
    elif(key == 5):
        if(qlsv.soLuongSinhVien() > 0):
            print("\n5. Sap xep sinh vien theo diem trung binh.")
            qlsv.sortByDiemTB()
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("\nDanh sach sinh vien rong. Vui long them sinh vien.")
    elif(key == 6):
        if(qlsv.soLuongSinhVien() > 0):
            print("\n6. Sap xep sinh vien theo ten chuyen nganh.")
            qlsv.sortByName()
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("\nDanh sach sinh vien rong. Vui long them sinh vien.")
    elif(key == 7):
        if(qlsv.soLuongSinhVien() > 0):
            print("\n7. Hien thi danh sach sinh vien.")
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("\nDanh sach sinh vien rong. Vui long them sinh vien.")
    elif(key == 0):
        print("\nBan da chon thoat chuong trinh!")
        break
    else:
        print("\nKhong co chuc nang nay.")
        print("\nHay chon chuc nang co trong menu.")
