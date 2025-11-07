import { useEffect, useState } from "react";
import "./AdminDashboard.css"
export default function AdminDashboard() {
  const [products, setProducts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  async function getProducts() {
    try {
      const response = await fetch("http://127.0.0.1:8000/products");

      if (!response.ok) {
        throw new Error("Encountered an issue while fetching products");
      }

      const data = await response.json();
      setProducts(data.products || []); // assuming backend returns {"products": [...]}
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  }

  async function Delete(id) {
  try {
    const token = localStorage.getItem("token"); // or sessionStorage depending on your setup

    const response = await fetch("http://127.0.0.1:8000/delete", {
  method: "DELETE",
  headers: {
    "Content-Type": "application/json",
    "Authorization": `Bearer ${token}`,
  },
  body: JSON.stringify({ id: id}),
});



    console.log("Response status:", response.status);

    if (!response.ok) {
      throw new Error("Error occured while executing!");
    }

    const data = await response.json();
    console.log("Delete success:", data);
    getProducts();
    return data;
  } catch (error) {
    console.error(error);
    throw error;
  }
}



  useEffect(() => {
    getProducts();
  }, []);

  if (loading) return <p>Loading products...</p>;
  if (error) return <p>Error: {error}</p>;

  return (
    <div className="container">
      <h2>Welcome Ajee's Store</h2>
      <p>Feel free to splurge</p>
      {products.length === 0 ? (
        <p>No products found.</p>
      ) : (
        <div className="product-list">
          {products.map((product) => (
            <div key={product.id} className="product-card">
                <button className="del-button" onClick={() => Delete(product.id)}>🗑️</button>
                <p>{product.name}</p>
                <p>{product.category}</p>
                <p>{product.price.toLocaleString()}</p>
                <p>{product.quantity}</p>

                <button className="add-to-cart-btn">Add to cart</button>
            </div>
            
          ))}
        </div>
      )}
    </div>
  );
}
