import csv

# This list was created by the chatgpt
qa_pairs = [
    ['bạn khỏe không', 'tôi khỏe, cảm ơn bạn đã hỏi'],
    ['bạn tên là gì', 'tôi là ChatGPT, một mô hình ngôn ngữ của OpenAI'],
    ['hôm nay trời thế nào', 'tôi không thể cung cấp thông tin thời tiết hiện tại'],
    ['bạn có thể làm gì', 'tôi có thể giúp bạn trả lời câu hỏi, viết văn bản, và nhiều hơn nữa'],
    ['ai là tổng thống của Việt Nam', 'đến thời điểm cuối cùng tôi được cập nhật, tôi không có thông tin cụ thể về cá nhân hiện thời'],
    ['python là gì', 'Python là một ngôn ngữ lập trình cấp cao, được sử dụng rộng rãi với mục đích tổng quát'],
    ['hà nội thuộc quốc gia nào', 'Hà Nội là thủ đô của Việt Nam'],
    ['bạn có thể nói tiếng việt không', 'tôi có thể giao tiếp bằng tiếng Việt'],
    ['việt nam có bao nhiêu tỉnh thành', 'Việt Nam có 63 tỉnh thành, bao gồm tỉnh và thành phố trực thuộc trung ương'],
    ['đồng hồ bao nhiêu rồi', 'tôi không thể cung cấp thời gian thực'],
    ['lập trình viên cần biết những gì', 'lập trình viên cần biết về ngôn ngữ lập trình, giải quyết vấn đề, cấu trúc dữ liệu và thuật toán'],
    ['python có mấy loại dữ liệu cơ bản', 'Python hỗ trợ nhiều loại dữ liệu cơ bản, bao gồm int, float, bool, str, list, tuple, set, và dict'],
    ['học lập trình bắt đầu từ đâu', 'bắt đầu học lập trình với ngôn ngữ Python là một lựa chọn tốt vì nó có cú pháp đơn giản và rõ ràng'],
    ['bạn khỏe không', 'tôi khỏe'],
    ['bạn tên là gì', 'tên tôi là ChatGPT'],
    ['bạn bao nhiêu tuổi', 'tôi là một mô hình AI và không có tuổi'],
    ['hôm nay thời tiết thế nào', 'tôi không thể cung cấp thông tin thời tiết thực tế'],
    ['việt nam có bao nhiêu tỉnh thành', 'việt nam có 63 tỉnh thành'],
    ['hà nội là thủ đô của quốc gia nào', 'hà nội là thủ đô của việt nam'],
    ['ai là tác giả của bài hát "Quốc ca Việt Nam"', 'tác giả là Văn Cao'],
    ['phở là món ăn đặc trưng của vùng nào ở việt nam', 'phở là món ăn đặc trưng của việt nam, đặc biệt là hà nội'],
    ['bánh mì có xuất xứ từ đâu', 'bánh mì có xuất xứ từ việt nam, phổ biến từ thời kỳ thuộc địa Pháp'],
    ['đồng bằng sông cửu long ở đâu', 'đồng bằng sông cửu long ở miền nam việt nam'],
    ['núi phú sĩ ở đâu', 'núi phú sĩ ở nhật bản'],
    ['sông nile dài bao nhiêu', 'sông nile dài khoảng 6,650 km'],
    ['đỉnh everest cao bao nhiêu', 'đỉnh everest cao 8,848 mét'],
    ['lễ hội té nước được tổ chức ở quốc gia nào', 'lễ hội té nước được tổ chức ở Thái Lan'],
    ['trái đất quay quanh mặt trời mất bao lâu', 'trái đất quay quanh mặt trời mất khoảng 365.25 ngày'],
    ['việt nam độc lập năm nào', 'việt nam độc lập vào năm 1945'],
    ['bài hát "Hà Nội Niềm Tin Và Hy Vọng" do ai sáng tác', 'bài hát "Hà Nội Niềm Tin Và Hy Vọng" do nhạc sĩ Trần Tiến sáng tác'],
    ['ai là người phát minh ra bóng đèn', 'người phát minh ra bóng đèn là Thomas Edison'],
    ['internet ra đời vào năm nào', 'internet ra đời vào năm 1969'],
    ['điện thoại di động đầu tiên trên thế giới ra đời năm nào', 'điện thoại di động đầu tiên trên thế giới ra đời vào năm 1973'],
    ['bitcoin được tạo ra bởi ai', 'bitcoin được tạo ra bởi một người hoặc nhóm người dùng bí danh Satoshi Nakamoto'],
    ['sách "Tắt đèn" được viết bởi ai', 'sách "Tắt đèn" được viết bởi nhà văn Ngô Tất Tố'],
    ['vạn lý trường thành được xây dựng để làm gì', 'vạn lý trường thành được xây dựng để bảo vệ đất nước khỏi các cuộc xâm lược của bộ lạc từ phía bắc'],
    ['loài chim không bao giờ hạ cánh là gì', 'loài chim không bao giờ hạ cánh là chim én biển'],
    ['sao thổ có bao nhiêu vệ tinh', 'sao thổ có 82 vệ tinh đã được xác nhận tính đến năm 2023'],
    ['nguồn gốc của ngày cá tháng tư là gì', 'nguồn gốc của ngày cá tháng tư không rõ ràng, nhưng nó được cho là đã xuất hiện từ thời Phục hưng ở châu Âu'],
    ['olympic đầu tiên được tổ chức khi nào', 'olympic đầu tiên được tổ chức vào năm 1896 tại Athens, Hy Lạp'],
    ['việt nam có mấy mùa trong năm', 'việt nam có bốn mùa ở miền bắc và hai mùa ở miền nam'],
    ['tiếng việt có bao nhiêu chữ cái', 'tiếng việt có 29 chữ cái'],
    ['lễ hội đền hùng diễn ra vào ngày nào', 'lễ hội đền hùng diễn ra vào ngày 10 tháng 3 âm lịch hàng năm'],
    ['sapa thuộc tỉnh nào của việt nam', 'sapa thuộc tỉnh lào cai'],
    ['vịnh hạ long thuộc tỉnh nào', 'vịnh hạ long thuộc tỉnh quảng ninh'],
    ['điểm cao nhất việt nam là đỉnh nào', 'điểm cao nhất việt nam là đỉnh Fansipan'],
    ['bài hát "Hòn vọng phu" do ai sáng tác', 'bài hát "Hòn vọng phu" do nhạc sĩ Lê Thương sáng tác'],
    ['ai là tác giả của tác phẩm "Tắt đèn"', 'tác giả của tác phẩm "Tắt đèn" là nhà văn Ngô Tất Tố'],
    ['cuộc chiến tranh biên giới phía bắc diễn ra vào năm nào', 'cuộc chiến tranh biên giới phía bắc diễn ra vào năm 1979'],
    ['bán đảo sơn trà ở đâu', 'bán đảo sơn trà ở đà nẵng'],
    ['nước việt nam có bao nhiêu dân tộc', 'nước việt nam có 54 dân tộc'],
    ['ngày giải phóng miền nam là ngày nào', 'ngày giải phóng miền nam là ngày 30 tháng 4 năm 1975'],
    ['ai là người viết quốc hiệu "Việt Nam"', 'quốc hiệu "Việt Nam" được đặt bởi Hoàng đế Gia Long'],
    ['quảng trường ba đình ở đâu', 'quảng trường ba đình ở hà nội'],
    ['"Thần đồng đất việt" là tác phẩm truyện tranh của ai', '"Thần đồng đất việt" là tác phẩm của Lê Linh và Nguyễn Khánh Dương'],
    ['chủ tịch hồ chí minh sinh năm bao nhiêu', 'chủ tịch hồ chí minh sinh ngày 19 tháng 5 năm 1890'],
    ['chủ tịch hồ chí minh mất năm nào', 'chủ tịch hồ chí minh mất ngày 2 tháng 9 năm 1969'],
    ['tên thật của chủ tịch hồ chí minh là gì', 'tên thật của ông là nguyễn sinh cung'],
    ['chủ tịch hồ chí minh đã từng sống ở những quốc gia nào', 'ông đã từng sống ở pháp, anh, liên xô, trung quốc, và một số quốc gia khác'],
    ['chủ tịch hồ chí minh tuyên bố độc lập cho việt nam ở đâu', 'ông tuyên bố độc lập cho việt nam tại quảng trường ba đình, hà nội vào ngày 2 tháng 9 năm 1945'],
    ['bảo tàng hồ chí minh ở đâu', 'bảo tàng hồ chí minh nằm ở hà nội'],
    ['cuốn sách nào được biết đến là tác phẩm viết về cuộc đời và sự nghiệp của chủ tịch hồ chí minh', '"Hồ Chí Minh: Một cuộc đời" là cuốn sách nổi tiếng viết về cuộc đời và sự nghiệp của ông'],
    ['hồ chí minh đã sử dụng bao nhiêu bí danh trong đời mình', 'chủ tịch hồ chí minh đã sử dụng khoảng hơn 50 bí danh trong đời mình'],
    ['chủ tịch hồ chí minh ký tên dưới bản tuyên ngôn độc lập của việt nam với bí danh nào', 'ông ký tên dưới bản tuyên ngôn độc lập với bí danh "Hồ Chí Minh"'],
    ['làng sen, nơi chủ tịch hồ chí minh sinh ra, thuộc tỉnh nào của việt nam', 'làng sen thuộc tỉnh nghệ an'],
    ['chủ tịch hồ chí minh là người đầu tiên nào kêu gọi dân tộc việt nam phải sống ra sao', 'chủ tịch hồ chí minh là người đầu tiên kêu gọi dân tộc việt nam sống hòa bình, độc lập, và hạnh phúc'],
    ['hồ chí minh thành lập tổ chức cách mạng nào', 'chủ tịch hồ chí minh thành lập tổ chức cách mạng việt nam độc lập đồng minh'],
    ['lực lượng nào dưới sự lãnh đạo của chủ tịch hồ chí minh chiến thắng ở diên biên phủ', 'lực lượng việt minh dưới sự lãnh đạo của chủ tịch hồ chí minh chiến thắng ở diên biên phủ'],
    ['chủ tịch hồ chí minh đã tuyên bố gì trong cuộc biểu tình tại quảng trường ba đình năm 1945', 'trong cuộc biểu tình tại quảng trường ba đình năm 1945, chủ tịch hồ chí minh tuyên bố độc lập cho việt nam'],
    ['chủ tịch hồ chí minh có thời gian sống ở bắc kinh không', 'có, ông đã sống ở bắc kinh trong một thời gian'],
    ['hồ chí minh ủng hộ phong trào giải phóng quốc tế nào', 'chủ tịch hồ chí minh ủng hộ phong trào giải phóng quốc tế, đặc biệt là ủng hộ phong trào giải phóng dân tộc ở các nước đang bị thực dân'],
    ['chủ tịch hồ chí minh được tôn vinh ở quốc gia nào với tên gọi "ông bác hồ"', 'chủ tịch hồ chí minh được tôn vinh ở việt nam với tên gọi "ông bác hồ"'],
    ['chủ tịch hồ chí minh có mối quan hệ gì với mahatma gandhi', 'chủ tịch hồ chí minh có mối quan hệ tốt với mahatma gandhi và họ cùng chia sẻ tư tưởng về đấu tranh cho độc lập và tự do dân tộc'],
    ['tên của hải quân việt nam được đặt theo tên gì của chủ tịch hồ chí minh', 'tên của hải quân việt nam được đặt theo tên gọi "quân đội nhân dân việt nam hải quân, với tên gọi ngắn gọn là hải quân nhân dân"'],
    ['quốc hội việt nam đã đặt tên cho tháng nào là "tháng chủ tịch hồ chí minh"', 'quốc hội việt nam đã đặt tên cho tháng 5 là "tháng chủ tịch hồ chí minh" để tưởng nhớ và tôn vinh ông'],
    ['chủ tịch hồ chí minh đã được tôn vinh như thế nào sau khi mất', 'sau khi mất, chủ tịch hồ chí minh được tôn vinh bằng việc đặt tên ông cho nhiều công trình, địa danh, và được tưởng nhớ trong nhiều dịp lễ và ngày kỷ niệm'],
    ['chủ tịch hồ chí minh đã nói câu nào về giáo dục', 'chủ tịch hồ chí minh đã nói: "giáo dục là một vấn đề quốc gia, là công việc của cả dân tộc và cả nước phải cùng làm"'],
    ['hồ chí minh đã từng làm nghề gì ở nước ngoài', 'trước khi trở thành lãnh đạo cách mạng, chủ tịch hồ chí minh đã từng làm công nhân, thợ lặn, và làm nhiều nghề khác trong nước ngoài'],
    ['bảo tàng nào ở hà nội chứa nhiều hiện vật liên quan đến cuộc đời của chủ tịch hồ chí minh', 'bảo tàng lịch sử quốc gia việt nam ở hà nội chứa nhiều hiện vật và tư liệu quý về cuộc đời của chủ tịch hồ chí minh'],
    ['chủ tịch hồ chí minh đã ra đi từ cuộc đời như thế nào', 'chủ tịch hồ chí minh đã ra đi vào ngày 2 tháng 9 năm 1969 tại hà nội do bệnh tình'],
    ['chủ tịch hồ chí minh được tôn vinh như thế nào trong văn hóa dân tộc việt nam', 'chủ tịch hồ chí minh được tôn vinh trong văn hóa dân tộc việt nam thông qua các bài hát, tác phẩm văn học, hình ảnh, và các sự kiện kỷ niệm'],
    ['chủ tịch hồ chí minh có mối quan hệ như thế nào với lãnh tụ cách mạng trung quốc mao trạch đông', 'chủ tịch hồ chí minh và lãnh tụ cách mạng trung quốc mao trạch đông có mối quan hệ tốt, họ là những người đồng minh trong cuộc đấu tranh cho độc lập và tự do của các nước Á Đông'],
    ['công ty in tiền quốc gia việt nam ra đời dưới thời chủ tịch hồ chí minh vào năm nào', 'công ty in tiền quốc gia việt nam ra đời vào năm 1945 dưới thời chủ tịch hồ chí minh'],
    ['quốc hội việt nam đã đặt tên cho đường nào tại hà nội theo tên gọi của chủ tịch hồ chí minh', 'quốc hội việt nam đã đặt tên cho đường "đường hồ chí minh" tại hà nội để tưởng nhớ ông'],
    ['Bạn cảm thấy thế nào hôm nay?', 'Tôi cảm thấy khá tốt, cảm ơn bạn đã hỏi.'],
    ['Bạn đã ăn sáng chưa?', 'Vâng, tôi đã ăn sáng rồi.'],
    ['Bạn đã làm gì vào cuối tuần vừa qua?', 'Cuối tuần vừa qua, tôi đã đi xem phim cùng bạn bè.'],
    ['Bạn có kế hoạch gì cho ngày mai không?', 'Ngày mai, tôi có kế hoạch đi dạo cùng gia đình.'],
    ['Bạn thích xem phim thể loại gì?', 'Tôi thích xem phim hành động và hài hước nhất.'],
    ['Bạn có thích đọc sách không?', 'Vâng, tôi rất thích đọc sách.'],
    ['Bạn thường ngủ mấy giờ mỗi đêm?', 'Tôi thường ngủ khoảng 7 đến 8 giờ mỗi đêm.'],
    ['Bạn thích đi du lịch đến đâu nhất?', 'Tôi thích đi du lịch đến những nơi có cảnh đẹp tự nhiên và văn hóa độc đáo.'],
    ['Bạn đã gặp bạn bè của mình gần đây chưa?', 'Vâng, tôi đã gặp bạn bè của mình vào cuối tuần trước.'],
    ['Bạn có thích nấu ăn không?', 'Vâng, tôi thích nấu ăn và thử nghiệm các món mới.'],
    ['Tôi buồn quá.', 'Hãy nhớ rằng bạn không phải đối mặt với mọi thứ một mình. Bạn có thể chia sẻ cảm xúc của mình với bạn bè hoặc người thân.'],
    ['Tôi cảm thấy mất động lực.', 'Mất động lực là một phần tự nhiên của cuộc sống. Hãy nghỉ ngơi và tìm lại nguồn động lực từ những nguồn ngoại cảnh như sách, video, hoặc bài học từ người khác.'],
    ['Tôi không biết phải làm gì.', 'Hãy nhớ rằng không ai có thể biết mọi thứ. Hãy dành thời gian để tự suy nghĩ và nghiên cứu trước khi ra quyết định.'],
    ['Tôi cảm thấy bất lực trước một thách thức lớn.', 'Hãy nhớ rằng mọi thách thức đều có giải pháp. Hãy chia nhỏ vấn đề thành các phần nhỏ hơn và tiến từng bước một.'],
    ['Tôi không biết làm thế nào để vượt qua một khó khăn.', 'Hãy tìm kiếm sự giúp đỡ từ người thân, bạn bè hoặc chuyên gia trong lĩnh vực liên quan. Đừng ngần ngại xin giúp đỡ khi cần.'],
    ['Tôi cảm thấy mệt mỏi với công việc.', 'Hãy nhớ rằng nghỉ ngơi và tái sức là quan trọng để duy trì hiệu suất làm việc tốt nhất. Hãy sắp xếp thời gian nghỉ ngơi và giữ lịch trình làm việc hợp lý.'],
    ['Tôi không có đủ tự tin để thử một điều mới.', 'Tự tin không phải là một điều tự nhiên mà có thể phát triển theo thời gian. Hãy thử thách bản thân và nhớ rằng thất bại là phần của quá trình học tập.'],
    ['Tôi lo lắng về tương lai.', 'Lo lắng về tương lai là điều tự nhiên. Hãy tập trung vào những gì bạn có thể kiểm soát ngay bây giờ và hãy tin rằng mọi thứ sẽ ổn thôi.'],
    ['Tôi không biết làm thế nào để giải quyết một mối quan hệ.', 'Hãy mở lòng và chia sẻ cảm xúc của bạn với người đó. Hãy lắng nghe và cố gắng hiểu quan điểm của nhau để tìm ra giải pháp phù hợp nhất.'],
    ['Tôi cảm thấy mất kiên nhẫn.', 'Kiên nhẫn là một kỹ năng có thể phát triển theo thời gian. Hãy nhớ rằng mọi thứ đều cần thời gian và nỗ lực để đạt được.'],
    ['Một tuần có bao nhiêu ngày?', 'Một tuần có 7 ngày.'],
    ['Một giờ có bao nhiêu phút?', 'Một giờ có 60 phút.'],
    ['Một phút có bao nhiêu giây?', 'Một phút có 60 giây.'],
    ['Một năm nhuận xuất hiện sau mấy năm?', 'Một năm nhuận xuất hiện sau mỗi 4 năm.'],
    ['Một thập kỷ bao nhiêu năm?', 'Một thập kỷ bao gồm 10 năm.'],
    ['Một thế kỷ bao nhiêu năm?', 'Một thế kỷ bao gồm 100 năm.'],
    ['Một ngày có bao nhiêu giờ?', 'Một ngày có 24 giờ.'],
    ['Một tháng có bao nhiêu ngày?', 'Số ngày trong một tháng thường thay đổi, nhưng có thể là 28, 29, 30 hoặc 31 ngày tùy thuộc vào tháng đó.'],
    ['Một tuần là bao nhiêu phần trăm của một năm?', 'Một tuần chiếm khoảng 1/52 (khoảng 1.923%) của một năm.'],
    ['Một năm là bao nhiêu phần trăm của một thế kỷ?', 'Một năm chiếm 1% của một thế kỷ.'],
    ['Một tuần có bao nhiêu giờ?', 'Một tuần có 168 giờ (7 ngày * 24 giờ/ngày).'],
    ['Một tháng có bao nhiêu tuần?', 'Tháng có thể có 4 hoặc 5 tuần, tùy thuộc vào tháng đó và cách tính của bạn.'],
    ['Một năm có bao nhiêu tháng?', 'Một năm có 12 tháng.'],
    ['Một thập kỷ bao nhiêu tháng?', 'Một thập kỷ bao gồm 120 tháng (10 năm * 12 tháng/năm).'],
    ['Một thế kỷ bao nhiêu tháng?', 'Một thế kỷ bao gồm 1200 tháng (100 năm * 12 tháng/năm).'],
    ['Một ngày bao nhiêu giây?', 'Một ngày có 86400 giây (24 giờ * 60 phút/giờ * 60 giây/phút).'],
    ['Một giờ bao nhiêu phút?', 'Một giờ có 60 phút.'],
    ['Một phút bao nhiêu mili giây?', 'Một phút có 60000 mili giây (60 giây * 1000 mili giây/giây).'],
    ['Một năm bao nhiêu tuần?', 'Một năm có khoảng 52 tuần (365 ngày / 7 ngày/tuần).'],
    ['Một tháng bao nhiêu ngày?', 'Tháng có thể có 28, 29, 30 hoặc 31 ngày, tùy thuộc vào tháng đó.'],
    ['Một giây bằng bao nhiêu mili giây?', 'Một giây bằng 1000 mili giây.'],
    ['Một phút bằng bao nhiêu giây?', 'Một phút bằng 60 giây.'],
    ['Một giờ bằng bao nhiêu phút?', 'Một giờ bằng 60 phút.'],
    ['Một ngày bằng bao nhiêu giờ?', 'Một ngày bằng 24 giờ.'],
    ['Một tuần bằng bao nhiêu ngày?', 'Một tuần bằng 7 ngày.'],
    ['Một tháng bằng bao nhiêu ngày?', 'Số ngày trong một tháng thường thay đổi, có thể là 28, 29, 30 hoặc 31 ngày.'],
    ['Một năm nhuận có bao nhiêu ngày?', 'Một năm nhuận có 366 ngày.'],
    ['Một năm không nhuận có bao nhiêu ngày?', 'Một năm không nhuận có 365 ngày.'],
    ['Một tháng có bao nhiêu tuần?', 'Tháng có thể có từ 4 đến 5 tuần, tùy thuộc vào số ngày trong tháng.'],
    ['Một năm có bao nhiêu tháng có 31 ngày?', 'Một năm có 7 tháng có 31 ngày.'],
    ['Một tuần bằng bao nhiêu phút?', 'Một tuần bằng 10080 phút (7 ngày * 24 giờ/ngày * 60 phút/giờ).'],
    ['Một tháng bằng bao nhiêu giờ?', 'Số giờ trong một tháng thường thay đổi tùy thuộc vào số ngày trong tháng đó.'],
    ['Một năm bằng bao nhiêu phút?', 'Một năm bằng 525600 phút (365 ngày * 24 giờ/ngày * 60 phút/giờ).'],
    ['Một thế kỷ bằng bao nhiêu năm?', 'Một thế kỷ bằng 100 năm.'],
    ['Một nghìn năm bằng bao nhiêu thế kỷ?', 'Một nghìn năm bằng 10 thế kỷ.'],
    ['Một thế kỷ bằng bao nhiêu ngày?', 'Một thế kỷ bằng khoảng 36525 ngày (100 năm * 365.25 ngày/năm).'],
    ['Một giờ bằng bao nhiêu mili giây?', 'Một giờ bằng 3600000 mili giây (60 phút * 60 giây/phút * 1000 mili giây/giây).'],
    ['Một năm nhuận có bao nhiêu ngày thêm?', 'Một năm nhuận có 1 ngày nhiều hơn so với năm không nhuận, tức là 366 ngày.'],
    ['Một năm có bao nhiêu giây?', 'Một năm bằng 31536000 giây (365 ngày * 24 giờ/ngày * 60 phút/giờ * 60 giây/phút).'],
    ['Một tuần bằng bao nhiêu giây?', 'Một tuần bằng 604800 giây (7 ngày * 24 giờ/ngày * 60 phút/giờ * 60 giây/phút).'],
]

f_txt = open('data/question_answer.txt','a', encoding='utf-8')
f_csv = open('data/question_answer.csv','a',encoding="utf-8")
writer = csv.writer(f_csv)

for pair in qa_pairs:
    f_txt.write(f'[Q] {pair[0]}[A] {pair[1]}')
    writer.writerow([pair[0],pair[1]])

f_txt.close()
f_csv.close()


