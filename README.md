# Python Web Parser

აღნიშნული მინი პროექტი შექმნილია Web Parsing თემაზე და წარმოადგენს 'ვებ-პარსერს'. მაგალითისთვის ავიღე ერთ-ერთი ქართული ინტერნეტ მაღაზიის ვებგვერდი (xiaomi.com.ge). კოდში შესაძლებელია ამ საიტის ნებისმიერი სხვა გვედის (განყოფილების) ლინკის ჩასმა, საიდანაც ამოიღებს და შეინახავს ინფორმაციას. პროგრამას გამოაქვს როგორც პროდუქტის დასახელება, ისე აქტუალური ფასი.

პროგრამა ითვლის კატეგორიაში არსებულ ყველა გვერდს და 'პარსავს' ყოველივე მათგანს, რის შემდეგადაც მიღებულ ინფორმაციას პაითონში ჩაშენებული CSV ფუნქციით ინახავს შესაბამისი ფაილის სახით (მიღებული ფაილის მაგალითი ატვირთულია ამავე რეპოზიტორიში) პროექტის საქაღალდეში. იმ შემთხვევაში, თუ კატეგორიაში ცოტა პროდუქტია და სულ ერთ გვერდზეა განლაგებული, პროგრამა არ 'დაიქრაშება' და ჩვეულებრივად შეინახავს მხოლოდ ამ გვერდზე არსებულ პროდუქტებს.

~ ტიმ სარქისიანი
