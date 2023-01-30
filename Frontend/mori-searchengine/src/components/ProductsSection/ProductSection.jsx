// Styles
import "../../assets/styles/css/ProductSection.css";
// Components
import Title from "../Title/Title";
import SecondTitle from "../Title/SecondTitle";
import TransparentButton from "../Button/TransparentButton";
import ProductCart from "./ProductCart/ProductCart";

function ProductsSection() {
  const productsData = [
    {
      id: 1,
      title: "پیراهن زمستانی جین وست",
      price: 400_000,
      delPrice: 599_000,
      img: "https://www.banimode.com/997754-large_default/92946.jpg",
      percent: 18,
    },
    {
      id: 2,
      title: "پیراهن مردانه زارا",
      price: 845_000,
      delPrice: 1_120_000,
      img: "https://www.banimode.com/440293-large_default/39328.jpg",
      percent: 24,
    },
    {
      id: 3,
      title: "پیراهن جدید فانتزی",
      price: 342_000,
      delPrice: 412_000,
      img: "https://www.banimode.com/210557-large_default/21151.jpg",
      percent: 37,
    },
    {
      id: 4,
      title: "پیراهن پسرانه راه راه",
      price: 178_000,
      delPrice: 320_000,
      img: "https://www.banimode.com/113135-large_default/12119.jpg",
      percent: 49,
    },
  ];

  return (
    <div className="products-section my-5 pt-4">
      <div className="row p-0 m-0">
        <div className="col-12 p-0 d-flex flex-column flex-lg-row align-items-lg-center justify-content-lg-between">
          <div>
            <Title title="محصولات تخفیف خورده" />
            <SecondTitle title="تخفیف های رویایی بر روی محصولات منتخب" />
          </div>
          <div>
            <TransparentButton title="مشاهده همه" iconName="arrow-left-3" />
          </div>
        </div>
        <div className="row w-100 p-0 m-0">
          <ProductCart {...productsData[0]} />
          <ProductCart {...productsData[1]} />
          <ProductCart {...productsData[2]} />
          <ProductCart {...productsData[3]} />
        </div>
      </div>
    </div>
  );
}

export default ProductsSection;
