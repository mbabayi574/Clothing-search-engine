import React, { useEffect } from "react";
import axios from "axios";

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
  const [page, setPage] = React.useState(1);
  const handlePageChange = (event, value) => {
    setPage(value);
    logProducts();
  };

  const [range_value, setRangeValue] = React.useState([1000, 59999999]);
  const rangeHandleChange = (event, newValue) => {
    setRangeValue(newValue);
  };

  const [checked, setChecked] = React.useState(false);
  const handleCheckedChange = (event) => {
    setChecked(event.target.checked);
  };

  const [ordering, setSort] = React.useState(0);
  const handleOrderingChange = (event) => {
    setSort(event.target.value);
    logProducts();
  };

  const [product_name, setProductName] = React.useState("");
  const [brand_name, setBrandName] = React.useState("");

  const handleProductNameChange = (event) => {
    setProductName(event.target.value);
  };

  const handleBrandNameChange = (event) => {
    setBrandName(event.target.value);
  };

  const logProducts = () => {
    // setResult(GetProducts());
    const url = "http://localhost:5000/products";

    const json_data = {
      page: page,
      limit: 12,
    };
    if (ordering == 0) {
      json_data.sort_flag = "none";
    }
    if (ordering == 1) {
      json_data.sort_flag = "asc";
    }
    if (ordering == 2) {
      json_data.sort_flag = "desc";
    }

    json_data.min_price = range_value[0];
    json_data.max_price = range_value[1];

    json_data.have_discount = checked;

    if (product_name == "") {
      json_data.product_name = ".*";
    } else {
      json_data.product_name = product_name;
    }
    if (brand_name == "") {
      json_data.brand_name = ".*";
    } else {
      json_data.brand_name = brand_name;
    }

    const config = {
      method: "post",
      url: url,
      headers: {
        "Content-Type": "application/json",
      },
      data: json_data,
    };

    axios(config)
      .then((response) => {
        console.log(response.data);
        setProductsData(response.data.products);
        setLastPage(response.data.last_page);
      })
      .catch((error) => {
        console.log(error);
      });
  };

  const [productsData, setProductsData] = React.useState([]);
  const [last_page, setLastPage] = React.useState(9999);

  // for first time excute logProducts
  useEffect(() => {
    logProducts();
  }, []);

  const handleRestartFilters = () => {
    // first set all filters to default then call logProducts ( it is async )
    setRangeValue([1000, 59999999]);
    setChecked(false);
    setSort(0);
    setProductName("");
    setBrandName("");
    logProducts();
  };

  return (
    <div className="products-section">
      <div className="row p-0 m-0">
        <div className="col-12 p-0 d-flex flex-column flex-lg-row align-items-lg-center justify-content-lg-between">
          <div>
            <Title title="نتایج" />
            <SecondTitle title="موری میگه احتمالا از محصولات زیر خوشت میاد 🥰" />
          </div>
          <div className="d-flex align-items-center" dir="ltr">
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
          </div>
        </div>
        <div className="col-xl-3 filter_section" dir="ltr">
          <TextField
            label="نام محصول"
            variant="outlined"
            fullWidth
            onChange={handleProductNameChange}
            value={product_name}
          />
          <div className="py-1"></div>
          <TextField
            label="نام برند"
            variant="outlined"
            fullWidth
            onChange={handleBrandNameChange}
            value={brand_name}
          />
          <div className="py-1"></div>
          <Typography id="range-slider" gutterBottom>
            محدوده قیمت
          </Typography>
          <Slider
            id="range-slider"
            valueLabelDisplay="auto"
            value={range_value}
            onChange={rangeHandleChange}
            min={1000}
            max={59999999}
          />
          <div className="py-1"></div>
          <FormControlLabel
            control={
              <Checkbox checked={checked} onChange={handleCheckedChange} />
            }
            label="تخفیف دار"
          />
          <div className="py-1"></div>
          <Button variant="contained" fullWidth onClick={logProducts}>
            اعمال فیلتر
          </Button>
          {/* a red button for restart filters */}
          <div className="py-1"></div>
          <Button
            variant="contained"
            color="error"
            fullWidth
            onClick={handleRestartFilters}
          >
            بازنشانی
          </Button>
        </div>

        {productsData && productsData.length > 0 ? (
          <div className="col-xl-9  row w-100 p-0 m-0 important-product-cart">
            {productsData.map((product) => (
              <ProductCart {...product} />
            ))}

            <div className="col-12 d-flex justify-content-center" dir="ltr">
              <Pagination
                page={page}
                count={last_page}
                color="primary"
                size="large"
                onChange={handlePageChange}
              />
            </div>
          </div>
        ) : (
          <div className="col-xl-9 d-flex justify-content-center align-items-center">
            <h1>محصولی یافت نشد</h1>
          </div>
        )}
      </div>
    </div>
  );
}

export default ProductsSection;
