/**
 * [harness] STAND-IN — NOT FROM THE DOCS. Added at the user's request.
 *
 * Both WebMCP samples (OrderSearch.vue, webmcp.ts) call a bare
 * `searchOrders(status)` that the page never defines. Their files are left
 * verbatim; instead, while a "stand-in" sample is open, this installs
 * `searchOrders` as a browser global, which is what that bare identifier
 * resolves to at call time. It is removed again when the sample unmounts, so
 * the verbatim samples keep failing exactly as published.
 *
 * Returns fixed sample orders filtered by the requested status — no real data,
 * no network.
 */
export type OrderStatus = "open" | "shipped" | "delivered";

const SAMPLE_ORDERS: { id: string; item: string; status: OrderStatus; total: number }[] = [
  { id: "ORD-1001", item: "Trail running shoes", status: "open", total: 129 },
  { id: "ORD-1002", item: "Rain jacket", status: "shipped", total: 89 },
  { id: "ORD-1003", item: "Water bottle", status: "delivered", total: 19 },
  { id: "ORD-1004", item: "Headlamp", status: "open", total: 45 },
  { id: "ORD-1005", item: "Trekking poles", status: "delivered", total: 74 },
];

async function searchOrders(status: OrderStatus) {
  return SAMPLE_ORDERS.filter((order) => order.status === status);
}

type Global = typeof globalThis & { searchOrders?: typeof searchOrders };

export function installSearchOrdersStandIn(): () => void {
  (globalThis as Global).searchOrders = searchOrders;
  return () => {
    delete (globalThis as Global).searchOrders;
  };
}
