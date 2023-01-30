import "../../assets/styles/css/Footer.css";
//Components
import Title from "../Title/Title";
import FooterOption from "./FooterOption";
import Enamad_Logo from "../../assets/Images/enamad.png";
import Samandehi_Logo from "../../assets/Images/samandehi.png";

export default function Footer() {
  const footerOptionsData = [
    {
      title: "تحویل رایگان",
      des: "سفارشات بالای 450 هزار تومان",
      iconName: "send",
    },
    { title: "مناسب‌ترین قیمت ها", des: "ارزانتر از همه جا", iconName: "cart" },
    { title: "امکان مقایسه", des: "بین کالاها و خدمات", iconName: "award" },
    {
      title: "پشتیبانی همه روزه",
      des: "پشتیبانی 7 روز هفته",
      iconName: "calling",
    },
  ];

  return (
    <footer>
      <div className="row m-0 p-0">
        <FooterOption {...footerOptionsData[0]} />
        <FooterOption {...footerOptionsData[1]} />
        <FooterOption {...footerOptionsData[2]} />
        <FooterOption {...footerOptionsData[3]} />
      </div>
      <div className="row p-0 m-0">
        <div className="col-12 p-0 m-0 mt-5 my-3">
          <Title title="موتور جستجوی موری" />
        </div>
        <div className="col-md-8 col-lg-9 p-0 m-0">
          موری یه موتور جستجو هست که میتونید ازش استفاده کنید تا کالاهایی که
          میخواید رو پیدا کنید. <br />
          این هوش مصنوعی بامزه میتونه با استفاده از سلایق شما و الگوریتم های
          یادگیری ماشین بهتون لباسی که با سلیقه شما جوره پیشنهاد کنه 😎
        </div>
        <div className="col-md-4 col-lg-3 p-0 m-0">
          <div className="row m-0 p-0 w-100  mt-4 mt-md-0 text-center">
            <div className="col-6 m-0 p-0">
              <img src={Enamad_Logo} className="img-fluid" alt="اینماد" />
            </div>
            <div className="col-6 m-0 p-0">
              <img src={Samandehi_Logo} className="img-fluid" alt="ساماندهی" />
            </div>
          </div>
        </div>
        <div
          className="copy font-m text-gray-dark col-12 my-5 text-center"
          dir="ltr"
        >
          The visual part of this program was done with the help of a project by{" "}
          <a href="https://github.com/alirezahoseini/banimode_landing_page">
            Mr. Alireza Hosseini
          </a>
          <br />
          Made with ❤️ By{" "}
          <a href="https://github.com/mbabayi574">Mohammadreza Babayi </a>
        </div>
      </div>
    </footer>
  );
}
