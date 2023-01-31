import { useState } from "react";
import HeadSection from "./components/HeadSection/HeadSection";
import ProductsSection from "./components/ProductsSection/ProductSection";
import Footer from "./components/Footer/Footer";

function App() {
  const [count, setCount] = useState(0);

  return (
    <div className="container-fluid px-lg-2">
      <HeadSection />
      <ProductsSection />
      <Footer />
    </div>
  );
}

export default App;
