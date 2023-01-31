import "../../assets/styles/css/Header.css";
import Mori_Logo from "../../assets/Images/Mori_Logo.png";

export default function Header() {
  return (
    <header className="w-100 px-0 mx-0 py-4">
      <div className="row px-3 mx-0 d-flex align-items-center justify-content-between justify-content-lg-start">
        <a href="#" className="logo">
          <img src={Mori_Logo} alt="Mori Logo" />
        </a>
        <div className="desktop-menu d-none d-lg-flex">
          <nav>
            <ul className="d-flex align-items-center m-0">
              <li className="mx-3">
                <a href="#">صفحه اصلی</a>
              </li>
              <li className="mx-3">
                <a href="#">تماس با ما</a>
              </li>
              <li className="mx-3">
                <a href="#">درباره ما</a>
              </li>
              <li className="mx-3">
                <a href="#">قوانین و مقرارت</a>
              </li>
            </ul>
          </nav>
        </div>
        <div className="mobile-menu d-flex d-lg-none">
          <i className="icon-light-menu-1 text-dark hamberger-btn"></i>
        </div>
      </div>
    </header>
  );
}
