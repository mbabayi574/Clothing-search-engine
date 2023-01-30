import React from "react";

// Styles
import "../../assets/styles/css/ProductSection.css";
// Components
import Title from "../Title/Title";
import SecondTitle from "../Title/SecondTitle";
import ProductCart from "./ProductCart/ProductCart";

// Pagination
import Pagination from "@mui/material/Pagination";

// TextField
import TextField from "@mui/material/TextField";

// Range Slider
import Slider from "@mui/material/Slider";

// Typography
import Typography from "@mui/material/Typography";

// Checkboxes
import FormControlLabel from "@mui/material/FormControlLabel";
import Checkbox from "@mui/material/Checkbox";

// Select
import Select from "@mui/material/Select";
import MenuItem from "@mui/material/MenuItem";
import FormControl from "@mui/material/FormControl";
import InputLabel from "@mui/material/InputLabel";

// Button
import Button from "@mui/material/Button";

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
    {
      id: 5,
      title: "پیراهن پسرانه راه راه",
      price: 178_000,
      delPrice: 320_000,
      img: "https://www.banimode.com/113135-large_default/12119.jpg",
      percent: 49,
    },
    {
      id: 6,
      title: "پیراهن پسرانه راه راه",
      price: 178_000,
      delPrice: 320_000,
      img: "https://www.banimode.com/113135-large_default/12119.jpg",
      percent: 49,
    },
    {
      id: 7,
      title: "پیراهن پسرانه راه راه",
      price: 178_000,
      delPrice: 320_000,
      img: "https://www.banimode.com/113135-large_default/12119.jpg",
      percent: 49,
    },
  ];

  const [range_value, setRangeValue] = React.useState([400000, 2000000]);
  const rangeHandleChange = (event, newValue) => {
    setRangeValue(newValue);
  };

  const [checked, setChecked] = React.useState(true);
  const handleCheckedChange = (event) => {
    setChecked(event.target.checked);
  };

  const [ordering, setSort] = React.useState(0);
  const handleOrderingChange = (event) => {
    setSort(event.target.value);
  };

  return (
    <div className="products-section">
      <div className="row p-0 m-0">
        <div className="col-12 p-0 d-flex flex-column flex-lg-row align-items-lg-center justify-content-lg-between">
          <div>
            <Title title="نتایج" />
            <SecondTitle title="موری میگه احتمالا از محصولات زیر خوشت میاد 🥰" />
          </div>
        </div>
        <div className="col-xl-3 filter_section" dir="ltr">
          <TextField label="نام محصول" variant="outlined" fullWidth />
          <div className="py-1"></div>
          <TextField label="نام برند" variant="outlined" fullWidth />
          <div className="py-1"></div>
          <Typography id="range-slider" gutterBottom>
            محدوده قیمت
          </Typography>
          <Slider
            id="range-slider"
            valueLabelDisplay="auto"
            value={range_value}
            onChange={rangeHandleChange}
            min={10000}
            max={200000000}
          />
          <div className="py-1"></div>
          <FormControlLabel
            control={
              <Checkbox checked={checked} onChange={handleCheckedChange} />
            }
            label="تخفیف دار"
          />

          <FormControl fullWidth>
            <InputLabel id="ordering-select-label">Order</InputLabel>
            <Select
              labelId="ordering-select-label"
              value={ordering}
              label="Order"
              onChange={handleOrderingChange}
            >
              <MenuItem value={0}>بدون مرتب سازی</MenuItem>
              <MenuItem value={1}>نزولی</MenuItem>
              <MenuItem value={2}>صعودی</MenuItem>
            </Select>
          </FormControl>

          <div className="py-1"></div>
          <Button variant="contained" fullWidth>
            اعمال فیلتر
          </Button>
        </div>
        <div className="col-xl-9  row w-100 p-0 m-0 important-product-cart">
          {productsData.map((product) => (
            <ProductCart {...product} />
          ))}
          <div className="col-12 d-flex justify-content-center" dir="ltr">
            <Pagination count={10} color="primary" size="large" />
          </div>
        </div>
      </div>
    </div>
  );
}

export default ProductsSection;
