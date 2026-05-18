export function tagURL(tag: string): string {
  if (["music", "projects", "pictures"].includes(tag)) {
    return `/${tag}`;
  } else {
    return `/tag/${tag}`;
  }
}
