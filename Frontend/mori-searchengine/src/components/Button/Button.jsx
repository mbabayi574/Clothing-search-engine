import "../../assets/styles/css/Button.css";

export default function Button({ title, iconName }) {
  return (
    <button type="button" className="button d-flex">
      <span>{title}</span>
      <i className={"icon-light-" + iconName}></i>
    </button>
  );
}
