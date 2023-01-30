export default function FooterOption({ iconName, title, des }) {
  return (
    <div className="footer-option my-2 col-md-6 col-lg-3 d-flex align-items-center p-0">
      <div className="icon-box d-flex align-items-center justify-content-center">
        <i className={"icon-light-" + iconName}></i>
      </div>
      <div className="body">
        <p className="font-lg text-second font-weight-bold m-0">{title}</p>
        <p className="font-m m-0 mt-2">{des}</p>
      </div>
    </div>
  );
}
