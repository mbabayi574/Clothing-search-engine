import "../../assets/styles/css/Button.css";

export default function TransparentButton({ title, iconName }) {
  return (
    <button type="button" className="transparent-button d-flex">
      <span>{title}</span>
      <i className={"icon-light-" + iconName}></i>
    </button>
  );
}
