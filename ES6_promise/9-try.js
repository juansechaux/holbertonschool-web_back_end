export default function guardrail(mathFunction) {
  const queue = [];
  try {
    const v = mathFunction();
    queue.push(v);
  } catch (e) {
    queue.push(e.toString());
  }
  queue.push('Guardrail was processed');
  return queue;
}
