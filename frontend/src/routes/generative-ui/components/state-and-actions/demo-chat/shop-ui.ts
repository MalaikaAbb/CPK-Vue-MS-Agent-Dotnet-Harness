// [harness] State and actions › “Run your code when users click”.
// The page prints this module without its imports; these lines are the only added lines.
import { z } from "zod";
import { createGenerativeUI } from "@copilotkit/vue/v2/generative-ui";
import ProductCard from "./components/ProductCard.vue";
// ── as published ──
export const shopUI = createGenerativeUI({
  id: "acme/shop@1",
  functions: {
    addToCart: {
      description: "Add a product to the cart",
      parameters: z.object({ productId: z.string(), quantity: z.number().default(1) }),
    },
  },
  components: {
    ProductCard: {
      component: ProductCard,
      props: z.object({ productId: z.string(), name: z.string() }),
      events: { onAddToCart: {} },
    },
  },
});
