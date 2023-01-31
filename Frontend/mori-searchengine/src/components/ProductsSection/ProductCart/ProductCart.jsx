import "../../../assets/styles/css/ProductCart.css";
import Price from "./Price";
import DeletedPrice from "./DeletedPrice";
import BadgeSticky from "./BadgeSticky";
import AddToCartButton from "../../Button/AddToCartButton";

export default function ProductCart({
  productName,
  imageShow,
  productDiscount = 0,
  price,
  productOldPrice,
  productUrl,
  productBrand,
}) {
  return (
    <div className="product-cart col-xl-3 col-md-4 col-6 p-2 p-lg-3 my-3 mx-auto">
      <a href={"https://www.banimode.com" + productUrl} className="cart-img">
        <img src={imageShow} className="mx-auto d-block" alt="product cart" />
        {productDiscount !== 0 && <BadgeSticky percent={productDiscount} />}
      </a>

      <div className="cart-body">
        <a
          className="cart-title"
          href={"https://www.banimode.com" + productUrl}
        >
          {productName}
          <br />
          {"(" + productBrand + ")"}
        </a>
        <div className="d-flex justify-content-between align-items-end">
          <a
            href={"https://www.banimode.com" + productUrl}
            className="add-cart-button d-flex align-items-center justify-content-center"
          >
            <AddToCartButton url={productUrl} />
          </a>

          <span className="d-inline-flex flex-column text-left">
            <DeletedPrice deletedPrice={productOldPrice} />
            <Price price={price} />
          </span>
        </div>
      </div>
    </div>
  );
}
