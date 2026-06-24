class RestaurantBill:
    def __init__(self, id, customer_name, table_number, food_amonut,vat_rate, service_fee,discount):
        self.id = id
        self.customer_name = customer_name
        self.table_number = table_number
        self.food_amonut = food_amonut
        self.vat_rate = vat_rate 
        self.service_fee = service_fee
        self.discount = discount

        self.total_bill = 0
        self.bill_type = []

        self.calculate_total_bill()
        self.classify_bill()

    def calculate_total_bill(self):
        self.total_bill = self.food_amonut + (self.food_amonut * self.vat_rate / 100) + self.service_fee - self.discount
    def classify_bill(self):
        if self.total_bill > 5_000_000:
            self.bill_type = "VIP"
        elif self.total_bill > 2_000_000:
            self.bill_type = "Lớn"
        elif self.total_bill > 500_000:
            self.bill_type = "Trung Bình"
        else:
            self.bill_type = "Nhỏ"
class RestaurantBillManager:
    def __init__(self):
        self.bills = []
    def find_id(self,b_id):
        for bill in self.bills:
            if bill.id.lower() == b_id.lower():
                return bill
        return None
    def validate_input(self,prompt, input_tpye : str = "str"):
        while True:
            user_input = input(prompt).strip()
            if not user_input:
                print("Không được để trống")
                continue
            if input_tpye == "str":
                return user_input
            elif input_tpye == "id":
                if self.find_id(user_input):
                    print("Mã hóa đơn không được trùng")
                    continue
                return user_input

            elif input_tpye == "amount":
                try:
                    value = int(user_input)
                    if value <= 0:
                        print("Tiền phải lớn hơn hoặc bằng 0!")
                        continue
                    return value
                except ValueError:
                    print("Nhập sai dữ liệu!")
            elif input_tpye == "vat":
                try:
                    value = int(user_input)
                    if value <= 0 or value > 100:
                        print("VAT từ 0 đến 100")
                        continue
                    return value
                except ValueError:
                    print("Nhập sai dữ liệu!")

    def show_all(self):
        if not self.bills:
            print("Danh sách đang trống")
            return

        print("-" * 180)
        print(
            f"{'Mã hóa đơn':<12}"
            f"{'Tên khách hàng':<15}"
            f"{'Số bàn':<15}"
            f"{'Tiền món ăn':<15}"
            f"{'Tỷ lệ VAT':<15}"
            f"{'Phí dịch vụ':<15}"
            f"{'Giảm giá':<15}"
            f"{'Tổng tiền hóa đơn':<15}"
            f"{'Phân loại hóa đơn':<15}"
        )
        print("-" * 180)

        for bill in self.bills:
            print(
                f"{bill.id:<12}"
                f"{bill.customer_name:<15}"
                f"{bill.table_number:<15}"
                f"{bill.food_amonut:<15}"
                f"{bill.vat_rate:<15}"
                f"{bill.service_fee:<15}"
                f"{bill.discount:<15}"
                f"{bill.total_bill:<15}"
                f"{bill.bill_type:<15}"
            )
    def add_b(self):
        print("=== Thêm hóa đơn ===")

        id = self.validate_input("Nhập Mã hóa đơn: ", "id")
        name = self.validate_input("Nhập tên khách hàng: ")
        table = self.validate_input("Nhập số bàn: ")
        amount = self.validate_input("Nhập tiền món ăn: ","amount")
        vat = self.validate_input("Nhập VAT: ", "vat")
        service = self.validate_input("Nhập phí dịch vụ: ", "amount")
        discount = self.validate_input("Nhập giảm giá: ", "amount")

        bill = RestaurantBill(
            id = id,
            customer_name = name,
            table_number = table,
            food_amonut = amount,
            vat_rate = vat,
            service_fee = service,
            discount = discount
        )
        self.bills.append(bill)
        print("Thêm hóa đơn bàn ăn thành công")
    def update_b(self):
        if not self.bills:
            print("Danh sách đang trống")
            return
        
        b_id = input("Nhập hóa đơn cần cập nhật: ").strip()

        bill = self.find_id(b_id)

        if not bill:
            print("Không tìm thấy hóa đơn cần cập nhật")
            return

        print("Cập nhật hóa đơn: ")

        bill.food_amonut = self.validate_input("Nhập tiền món ăn: ","amount")
        bill.vat_rate = self.validate_input("Nhập VAT: ","vat")
        bill.service_fee = self.validate_input("Nhập phí dịch vụ: ","amount")
        bill.food_amonut = self.validate_input("Nhập giảm giá: ","amount")
        bill.calculate_total_bill()
        bill.classify_bill()

        print("Cập nhật hóa đơn thành công!")
    def delete_b(self):
        if not self.bills:
            print("Danh sách đang trống")
            return

        b_id = input("Nhập hóa đơn cần xóa: ").strip()

        bill = self.find_id(b_id)

        if not bill:
            print("Không tìm thấy hóa đơn cần xóa!")
            return

        confirm = input("Bạn có chắc chắn xóa hóa đơn này không? (Y/N): ").strip().lower()

        if confirm == "y":
            self.bills.remove(bill)
            print("Xóa hóa đơn!")
        elif confirm == "n":
            print("Hủy thao tác")
        else:
            print("Lựa chọn không hợp lệ")
    def search_b(self):
        if not self.bills:
            print("Danh sách đang trống")
            return

        keyword = input("Nhập tên người hoặc số bàn cần tìm: ").strip().lower()

        result = []

        for bill in self.bills:
            if keyword in bill.customer_name.lower() and keyword in bill.table_number:
                result.append(bill)

        if not result:
            print("Không tìm thấy hóa đơn phù hợp")
            return

        print("-" * 180)
        print(
            f"{'Mã hóa đơn':<12}"
            f"{'Tên khách hàng':<25}"
            f"{'Số bàn':<15}"
            f"{'Tiền món ăn':<15}"
            f"{'Tỷ lệ VAT':<15}"
            f"{'Phí dịch vụ':<15}"
            f"{'Giảm giá':<15}"
            f"{'Tổng tiền hóa đơn':<20}"
            f"{'Phân loại hóa đơn':<30}"
        )
        print("-" * 180)

        for bill in self.bills:
            print(
                f"{bill.id:<12}"
                f"{bill.customer_name:<25}"
                f"{bill.table_number:<15}"
                f"{bill.food_amonut:<15}"
                f"{bill.vat_rate:<15}"
                f"{bill.service_fee:<15}"
                f"{bill.discount:<15}"
                f"{bill.total_bill:<20}"
                f"{bill.bill_type:<30}"
            )
def menu():
    print("=============== Menu ===============")
    print("1. Hiển thị danh sách hóa đơn bàn ăn")
    print("2. Thêm hóa đơn mới")
    print("3. Cập nhật hóa đơn")
    print("4. Xóa hóa đơn")
    print("5. Tìm kiếm hóa đơn")
    print("6. Thoát")
    print("====================================")
manager = RestaurantBillManager()
def main():
    while True:
        menu()
        choice = input("Nhập lựa chọn của bạn: ")

        match choice:
            case "1":
                manager.show_all()
            case "2":
                manager.add_b()
            case "3":
                manager.update_b()
            case "4":
                manager.delete_b()
            case "5":
                manager.search_b()
            case "6":
                print("Cảm ơn bạn đã sử dụng hệ thống quản lý nhà hàng!")
                break
            case _:
                print("Lựa chọn không hợp lệ")
main()


