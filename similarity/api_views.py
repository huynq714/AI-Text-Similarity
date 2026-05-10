from django.http import JsonResponse
import random


TEXTS = [

    # =========================================================
    # 10 CẶP CÓ NỘI DUNG TƯƠNG ĐỒNG
    # =========================================================

    (
        "Trí tuệ nhân tạo đang dần thay đổi cách con người làm việc và học tập trong thời đại công nghệ hiện nay. "
        "Nhiều doanh nghiệp đã sử dụng AI để tự động hóa quy trình, phân tích dữ liệu và nâng cao hiệu suất công việc. "
        "Ngoài ra, AI còn hỗ trợ giáo dục thông qua các hệ thống học tập thông minh và cá nhân hóa nội dung cho học sinh.",

        "AI hiện đại đang tạo ra nhiều thay đổi lớn trong cuộc sống và công việc của con người. "
        "Các công ty công nghệ ứng dụng trí tuệ nhân tạo để xử lý dữ liệu nhanh hơn và giảm khối lượng công việc thủ công. "
        "Trong giáo dục, những hệ thống học tập thông minh sử dụng AI giúp học sinh tiếp cận kiến thức hiệu quả hơn."
    ),

    (
        "Việc đọc sách mỗi ngày giúp con người mở rộng kiến thức và cải thiện khả năng tư duy logic một cách hiệu quả. "
        "Những cuốn sách về khoa học, lịch sử hoặc kỹ năng sống mang lại nhiều bài học giá trị cho người đọc. "
        "Ngoài ra, thói quen đọc sách còn giúp giảm căng thẳng và tăng khả năng tập trung trong công việc.",

        "Đọc sách thường xuyên là một thói quen tốt giúp nâng cao hiểu biết và phát triển khả năng suy nghĩ logic. "
        "Nhiều người lựa chọn đọc các loại sách về kỹ năng, khoa học hoặc lịch sử để học hỏi thêm kinh nghiệm sống. "
        "Không chỉ vậy, việc đọc sách còn giúp thư giãn tinh thần và cải thiện sự tập trung hiệu quả."
    ),

    (
        "Năng lượng mặt trời đang trở thành một trong những nguồn năng lượng sạch quan trọng nhất trên thế giới hiện nay. "
        "Việc sử dụng điện mặt trời giúp giảm lượng khí thải gây ô nhiễm môi trường và tiết kiệm tài nguyên thiên nhiên. "
        "Nhiều quốc gia đang đầu tư mạnh vào công nghệ năng lượng tái tạo để hướng đến phát triển bền vững.",

        "Điện mặt trời được xem là giải pháp năng lượng xanh giúp bảo vệ môi trường và giảm phụ thuộc vào nhiên liệu hóa thạch. "
        "Nguồn năng lượng tái tạo này giúp hạn chế khí thải độc hại và tiết kiệm tài nguyên thiên nhiên lâu dài. "
        "Hiện nay, nhiều nước trên thế giới đang đẩy mạnh đầu tư vào công nghệ năng lượng sạch."
    ),

    (
        "Tập thể dục thường xuyên mang lại nhiều lợi ích cho sức khỏe thể chất và tinh thần của con người. "
        "Các hoạt động như chạy bộ, bơi lội hoặc đạp xe giúp cải thiện tim mạch và tăng cường sức đề kháng. "
        "Ngoài ra, việc luyện tập đều đặn còn giúp giảm căng thẳng và cải thiện chất lượng giấc ngủ.",

        "Việc vận động thể thao đều đặn giúp cơ thể khỏe mạnh hơn và hạn chế nguy cơ mắc nhiều loại bệnh. "
        "Những bài tập như bơi lội, chạy bộ hay đạp xe có tác dụng tăng cường sức khỏe tim mạch và sức bền. "
        "Bên cạnh đó, luyện tập thể thao còn hỗ trợ giảm stress và giúp con người ngủ ngon hơn."
    ),

    (
        "Du lịch giúp con người khám phá nhiều nền văn hóa mới và mang lại những trải nghiệm đáng nhớ trong cuộc sống. "
        "Khi đến một quốc gia khác, mọi người có cơ hội tìm hiểu ẩm thực, phong tục và lối sống địa phương. "
        "Ngoài ra, du lịch còn giúp thư giãn tinh thần và tạo động lực tích cực cho công việc.",

        "Đi du lịch là cách tuyệt vời để khám phá văn hóa và trải nghiệm cuộc sống ở nhiều nơi khác nhau. "
        "Con người có thể tìm hiểu thêm về ẩm thực, con người và phong tục tại các vùng đất mới. "
        "Không chỉ giúp giải trí, du lịch còn giúp cải thiện tinh thần và tạo thêm cảm hứng trong cuộc sống."
    ),

    (
        "Internet đã thay đổi hoàn toàn cách con người giao tiếp, học tập và làm việc trong xã hội hiện đại. "
        "Nhờ internet, mọi người có thể dễ dàng tìm kiếm thông tin và kết nối với nhau trên toàn cầu. "
        "Các nền tảng trực tuyến hiện nay còn hỗ trợ học tập từ xa và làm việc online hiệu quả hơn.",

        "Mạng internet đóng vai trò rất quan trọng trong cuộc sống hiện đại của con người ngày nay. "
        "Nó giúp mọi người dễ dàng trao đổi thông tin, học tập và làm việc từ bất kỳ đâu trên thế giới. "
        "Bên cạnh đó, internet còn tạo điều kiện phát triển mạnh mẽ cho các nền tảng học tập và làm việc trực tuyến."
    ),

    (
        "Âm nhạc có khả năng giúp con người thư giãn tinh thần và giảm căng thẳng sau thời gian làm việc mệt mỏi. "
        "Nhiều người thường nghe nhạc vào buổi tối để cải thiện tâm trạng và lấy lại năng lượng tích cực. "
        "Ngoài ra, âm nhạc còn đóng vai trò quan trọng trong nghệ thuật và đời sống văn hóa.",

        "Nghe nhạc là phương pháp giải trí phổ biến giúp con người cảm thấy thoải mái và giảm áp lực trong cuộc sống. "
        "Những giai điệu nhẹ nhàng có thể cải thiện tâm trạng và giúp mọi người thư giãn sau ngày dài làm việc. "
        "Không chỉ là hình thức giải trí, âm nhạc còn có ý nghĩa lớn trong văn hóa và nghệ thuật."
    ),

    (
        "Điện toán đám mây giúp doanh nghiệp lưu trữ dữ liệu trực tuyến và quản lý thông tin hiệu quả hơn. "
        "Nhờ cloud computing, nhân viên có thể truy cập dữ liệu từ nhiều thiết bị và làm việc từ xa thuận tiện. "
        "Công nghệ này còn giúp tiết kiệm chi phí đầu tư cơ sở hạ tầng cho doanh nghiệp.",

        "Cloud computing đang được nhiều doanh nghiệp sử dụng để lưu trữ và quản lý dữ liệu trực tuyến. "
        "Công nghệ này cho phép người dùng truy cập thông tin linh hoạt từ nhiều nơi và nhiều thiết bị khác nhau. "
        "Ngoài ra, điện toán đám mây còn giúp công ty giảm chi phí vận hành hệ thống công nghệ."
    ),

    (
        "Học ngoại ngữ mang lại rất nhiều cơ hội nghề nghiệp và giúp con người giao tiếp tốt hơn với thế giới. "
        "Việc biết thêm nhiều ngôn ngữ giúp dễ dàng làm việc trong môi trường quốc tế và tiếp cận kiến thức mới. "
        "Ngoài ra, học ngoại ngữ còn giúp phát triển tư duy và tăng khả năng tự tin khi giao tiếp.",

        "Biết nhiều ngoại ngữ giúp con người có thêm cơ hội nghề nghiệp và thuận lợi trong giao tiếp quốc tế. "
        "Nhiều công việc hiện nay yêu cầu kỹ năng ngoại ngữ để làm việc với đối tác nước ngoài hiệu quả hơn. "
        "Không chỉ vậy, học ngôn ngữ mới còn giúp cải thiện tư duy và tăng sự tự tin trong cuộc sống."
    ),

    (
        "Blockchain là công nghệ lưu trữ dữ liệu phi tập trung giúp tăng tính minh bạch và bảo mật cho giao dịch điện tử. "
        "Thông tin trong blockchain được lưu trên nhiều hệ thống khác nhau nên rất khó bị thay đổi hoặc tấn công. "
        "Hiện nay, công nghệ này được ứng dụng rộng rãi trong tài chính và tiền điện tử.",

        "Công nghệ blockchain giúp lưu trữ dữ liệu an toàn và minh bạch nhờ cơ chế hoạt động phi tập trung. "
        "Dữ liệu được phân phối trên nhiều máy tính khác nhau nên hạn chế nguy cơ bị sửa đổi trái phép. "
        "Blockchain hiện đang được sử dụng phổ biến trong lĩnh vực tài chính và tiền mã hóa."
    ),


    # =========================================================
    # 10 CẶP KHÁC NHAU HOÀN TOÀN
    # =========================================================

    (
        "Bóng đá là môn thể thao được yêu thích nhất trên thế giới với hàng triệu người hâm mộ theo dõi mỗi năm. "
        "Các giải đấu lớn như World Cup hay Champions League luôn thu hút sự quan tâm rất lớn từ khán giả toàn cầu. "
        "Nhiều cầu thủ nổi tiếng đã trở thành biểu tượng thể thao và truyền cảm hứng cho giới trẻ.",

        "Thiên văn học là ngành khoa học nghiên cứu các hành tinh, ngôi sao và hiện tượng xảy ra ngoài không gian vũ trụ. "
        "Các nhà khoa học sử dụng kính thiên văn hiện đại để quan sát và tìm hiểu nguồn gốc của vũ trụ. "
        "Lĩnh vực này đóng vai trò quan trọng trong việc khám phá những bí ẩn của không gian."
    ),

    (
        "Nấu ăn là kỹ năng quan trọng giúp con người chuẩn bị những bữa ăn ngon và đảm bảo sức khỏe cho gia đình. "
        "Việc lựa chọn nguyên liệu sạch và chế biến đúng cách giúp tăng giá trị dinh dưỡng cho món ăn. "
        "Ngoài ra, nấu ăn còn được xem là một hoạt động thư giãn và sáng tạo trong cuộc sống.",

        "Lập trình phần mềm là quá trình xây dựng các ứng dụng và hệ thống công nghệ phục vụ nhu cầu của con người. "
        "Các lập trình viên sử dụng nhiều ngôn ngữ khác nhau để phát triển website, ứng dụng di động hoặc phần mềm máy tính. "
        "Ngành công nghệ thông tin hiện nay đang phát triển rất mạnh trên toàn thế giới."
    ),

    (
        "Mèo là loài động vật được nhiều người yêu thích vì vẻ ngoài dễ thương và tính cách thân thiện. "
        "Nhiều gia đình nuôi mèo như thú cưng để giúp cuộc sống trở nên vui vẻ và thoải mái hơn. "
        "Ngoài ra, mèo còn nổi tiếng với khả năng bắt chuột rất hiệu quả.",

        "Xe tải là phương tiện giao thông chuyên dùng để vận chuyển hàng hóa với tải trọng lớn trên đường bộ. "
        "Các doanh nghiệp logistics sử dụng nhiều loại xe tải khác nhau để giao hàng giữa các thành phố. "
        "Ngành vận tải đóng vai trò rất quan trọng trong nền kinh tế hiện đại."
    ),

]
def generate_random_texts(request):

    text1, text2 = random.choice(TEXTS)

    return JsonResponse({

        "success": True,

        "text1": text1,

        "text2": text2

    })